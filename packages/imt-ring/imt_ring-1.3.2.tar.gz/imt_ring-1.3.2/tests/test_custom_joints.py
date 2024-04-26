import jax
import numpy as np
import ring
from ring import MotionConfig
from ring.algorithms import custom_joints
from ring.algorithms.generator import transforms
from ring.algorithms.jcalc import _init_joint_params


def pipeline_load_data_X(
    sys: ring.System,
):
    sys_noimu, _ = sys.make_sys_noimu()

    gen = ring.algorithms.GeneratorPipe(
        transforms.GeneratorTrafoJointAxisSensor(sys_noimu),
        ring.algorithms.GeneratorTrafoRemoveOutputExtras(),
        ring.algorithms.GeneratorTrafoRemoveInputExtras(sys),
    )(MotionConfig(T=10.0))

    return gen(jax.random.PRNGKey(1))[0]


def test_virtual_input_joint_axes_rr_joint():
    sys = ring.io.load_example("test_three_seg_seg2")
    sys_rr = sys.replace(
        link_types=[
            "rr" if link_type in ["ry", "rz"] else link_type
            for link_type in sys.link_types
        ]
    )
    sys_rr = _init_joint_params(jax.random.PRNGKey(1), sys_rr)
    joint_axes = sys_rr.links.joint_params["rr"]["joint_axes"]

    # test `ry` / `rz`
    X = pipeline_load_data_X(sys)

    np.testing.assert_allclose(
        X["seg1"]["joint_axes"],
        np.repeat(np.array([[0.0, -1, 0]]), 1000, axis=0),
        atol=1e-7,
    )
    np.testing.assert_allclose(
        X["seg3"]["joint_axes"],
        np.repeat(np.array([[0.0, 0, 1]]), 1000, axis=0),
        atol=1e-7,
    )

    # test `rr`
    X = pipeline_load_data_X(sys_rr)

    np.testing.assert_allclose(
        X["seg1"]["joint_axes"],
        np.repeat(-joint_axes[1:2], 1000, axis=0),
        atol=3e-7,
        rtol=2e-6,
    )
    np.testing.assert_allclose(
        X["seg3"]["joint_axes"],
        np.repeat(joint_axes[3:4], 1000, axis=0),
        atol=3e-7,
        rtol=2e-6,
    )


def test_virtual_input_joint_axes_rr_imp_joint():
    custom_joints.register_rr_imp_joint(MotionConfig(T=10.0))

    sys = ring.io.load_example("test_three_seg_seg2")
    sys_rr_imp = sys.change_joint_type("seg1", "rr_imp").change_joint_type(
        "seg3", "rr_imp"
    )
    sys_rr_imp = _init_joint_params(jax.random.PRNGKey(1), sys_rr_imp)
    joint_axes = sys_rr_imp.links.joint_params["rr_imp"]["joint_axes"]

    # test `rr_imp`
    X = pipeline_load_data_X(sys_rr_imp)

    np.testing.assert_allclose(
        X["seg1"]["joint_axes"],
        np.repeat(joint_axes[1:2], 1000, axis=0),
        atol=0.01,
        rtol=0.02,
    )
    np.testing.assert_allclose(
        X["seg3"]["joint_axes"],
        np.repeat(-joint_axes[3:4], 1000, axis=0),
        atol=0.002,
        rtol=0.002,
    )

    # test `make_generator`
    # we can't really test behaviour for `rr_imp` since the `make_generator` internally
    # builds a `setup_fn` that randomizes the `sys.links.joint_params` field
    X = pipeline_load_data_X(sys)

    np.testing.assert_allclose(
        X["seg1"]["joint_axes"],
        np.repeat(np.array([[0.0, -1, 0]]), 1000, axis=0),
        atol=1e-7,
    )
    np.testing.assert_allclose(
        X["seg3"]["joint_axes"],
        np.repeat(np.array([[0.0, 0, 1]]), 1000, axis=0),
        atol=1e-7,
    )

from unittest import mock

import pytest

from bec_lib.scans import ScanObject


@pytest.fixture
def scan_obj(bec_client_mock):
    scan_info = {
        "class": "FermatSpiralScan",
        "arg_input": {"device": "device", "start": "float", "stop": "float"},
        "required_kwargs": ["step", "relative"],
        "arg_bundle_size": {"bundle": 3, "min": 2, "max": 2},
        "scan_report_hint": "table",
        "doc": (
            "\n        A scan following Fermat's spiral.\n\n        Args:\n            *args: pairs"
            " of device / start position / end position / steps arguments\n            relative:"
            " Start from an absolute or relative position\n            burst: number of acquisition"
            " per point\n            optim_trajectory: routine used for the trajectory"
            " optimization, e.g. 'corridor'. Default: None\n\n        Returns:\n\n       "
            " Examples:\n            >>> scans.fermat_scan(dev.motor1, -5, 5, dev.motor2, -5, 5,"
            ' step=0.5, exp_time=0.1, relative=True, optim_trajectory="corridor")\n\n        '
        ),
    }
    scan_name = "fermat_scan"
    obj = ScanObject(scan_name, scan_info, bec_client_mock)
    with mock.patch.object(bec_client_mock, "alarm_handler"):
        yield obj


@pytest.fixture
def dev(scan_obj):
    devices = scan_obj.client.device_manager.devices
    yield devices


def test_scan_object_raises(scan_obj):
    with pytest.raises(TypeError):
        scan_obj._run()


def test_scan_object_raises_not_enough_bundles(scan_obj, dev):
    with pytest.raises(TypeError):
        scan_obj._run(dev.samx, -5, 5, step=0.5, exp_time=0.1, relative=False)


def test_scan_object_raises_too_many_bundles(scan_obj, dev):
    with pytest.raises(TypeError):
        scan_obj._run(
            dev.samx,
            -5,
            5,
            dev.samy,
            -5,
            5,
            dev.samz,
            -5,
            5,
            step=0.5,
            exp_time=0.1,
            relative=False,
        )


def test_scan_object(scan_obj, dev):
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as report:
        scan_obj._run(dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False)
        report().wait.assert_not_called()


def test_scan_object_wo_live_updates(scan_obj, dev):
    scan_obj.client.live_updates = None
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as report:
        scan_obj._run(dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False)
        report().wait.assert_not_called()


def test_scan_object_file_suffix(scan_obj, dev):
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
        with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
            scan_obj._run(
                dev.samx,
                -5,
                5,
                dev.samy,
                -5,
                5,
                step=0.5,
                exp_time=0.1,
                relative=False,
                file_suffix="testsample",
            )
            assert (
                scan_report.call_args.args[0].metadata["file_writer_data"]["file_suffix"]
                == "testsample"
            )


@pytest.mark.parametrize(
    "file_suffix, file_suffix_raises",
    [
        ("testsample", False),
        ("testsample_", False),
        ("testsample-", False),
        ("ötestsample", True),
        ("123sample", False),
        ("../sample", True),
        ("sample/123", True),
        ("sample\\123", True),
        ("sample123\\", True),
        ("sample123/", True),
        ("sample123.", True),
    ],
)
def test_scan_object_raises_on_non_ascii_chars(scan_obj, dev, file_suffix, file_suffix_raises):
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
        with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
            if file_suffix_raises:
                with pytest.raises(ValueError):
                    scan_obj._run(
                        dev.samx,
                        -5,
                        5,
                        dev.samy,
                        -5,
                        5,
                        step=0.5,
                        exp_time=0.1,
                        relative=False,
                        file_suffix=file_suffix,
                    )
            else:
                scan_obj._run(
                    dev.samx,
                    -5,
                    5,
                    dev.samy,
                    -5,
                    5,
                    step=0.5,
                    exp_time=0.1,
                    relative=False,
                    file_suffix=file_suffix,
                )
                assert (
                    scan_report.call_args.args[0].metadata["file_writer_data"]["file_suffix"]
                    == file_suffix
                )


@pytest.mark.parametrize(
    "file_dir, file_suffix_raises",
    [
        ("/tmp/data/", False),
        ("/tmp/data./", True),
        ("/tmp/data-1/", False),
        ("/tmp/data_1/", False),
        ("sample\\123", True),
        ("//sample//123//", False),
    ],
)
def test_scan_object_raises_on_non_ascii_chars_dir(scan_obj, dev, file_dir, file_suffix_raises):
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
        with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
            if file_suffix_raises:
                with pytest.raises(ValueError):
                    scan_obj._run(
                        dev.samx,
                        -5,
                        5,
                        dev.samy,
                        -5,
                        5,
                        step=0.5,
                        exp_time=0.1,
                        relative=False,
                        file_directory=file_dir,
                    )
            else:
                scan_obj._run(
                    dev.samx,
                    -5,
                    5,
                    dev.samy,
                    -5,
                    5,
                    step=0.5,
                    exp_time=0.1,
                    relative=False,
                    file_directory=file_dir,
                )
                assert scan_report.call_args.args[0].metadata["file_writer_data"][
                    "file_directory"
                ] == file_dir.strip("/")


def test_scan_object_receives_sample_name(scan_obj, dev):
    with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
        with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
            scan_obj._run(dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False)
            assert scan_report.call_args.args[0].metadata["sample_name"] == "test_sample"


def test_scan_object_receives_scan_group(scan_obj, dev):
    scan_obj.client.scans._scan_group = "group_id"
    with mock.patch.object(scan_obj.client, "alarm_handler"):
        with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
            with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
                scan_obj._run(
                    dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False
                )
                assert scan_report.call_args.args[0].metadata["queue_group"] == "group_id"


def test_scan_object_receives_scan_def_id(scan_obj, dev):
    scan_obj.client.scans._scan_def_id = "scan_def_id"
    with mock.patch.object(scan_obj.client, "alarm_handler"):
        with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
            with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
                scan_obj._run(
                    dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False
                )
                assert scan_report.call_args.args[0].metadata["scan_def_id"] == "scan_def_id"


def test_scan_object_receives_dataset_id_on_hold(scan_obj, dev):
    scan_obj.client.scans._dataset_id_on_hold = "dataset_id_on_hold"
    with mock.patch.object(scan_obj.client, "alarm_handler"):
        with mock.patch("bec_lib.scan_report.ScanReport.from_request") as scan_report:
            with mock.patch.object(scan_obj.client, "get_global_var", return_value="test_sample"):
                scan_obj._run(
                    dev.samx, -5, 5, dev.samy, -5, 5, step=0.5, exp_time=0.1, relative=False
                )
                assert (
                    scan_report.call_args.args[0].metadata["dataset_id_on_hold"]
                    == "dataset_id_on_hold"
                )

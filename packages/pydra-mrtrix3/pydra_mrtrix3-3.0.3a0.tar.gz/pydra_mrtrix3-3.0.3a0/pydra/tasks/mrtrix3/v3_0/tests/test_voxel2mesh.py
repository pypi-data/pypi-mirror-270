# Auto-generated test for voxel2mesh

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import voxel2mesh


def test_voxel2mesh(tmp_path, cli_parse_only):

    task = voxel2mesh(
        in_file=Nifti1.sample(),
        out_file=File.sample(),
        blocky=True,
        threshold=1.0,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored

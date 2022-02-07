from petrelgridio.petrel_grid import PetrelGrid
from petrelgridio.raw_mesh import RawMesh
from petrelgridio.vtu import to_vtu

from utils import *


def test_export_to_vtu():
    # Test model
    name = "Simple20x20x5_Fault.grdecl"

    # Creates a PetrelGrid object
    grid = PetrelGrid.build_from_files(DATA_FOLDER + name)
    hexa, vertices, _, _ = grid.process()

    # Split at faults
    vertices, cells_faces, faces_nodes = grid.process_faults(hexa)

    # Creates and exports HybridMesh
    mesh = RawMesh(vertices=vertices, face_nodes=faces_nodes, cell_faces=cells_faces)
    mesh, original_cell = mesh.as_hybrid_mesh()
    print(f"Splitted {name} mesh with: {mesh.nb_vertices} vertices, {mesh.nb_cells} cells, {mesh.nb_faces} faces")
    to_vtu(mesh, OUTPUT_FOLDER + name + "_hybridmesh", celldata={"original_cell": original_cell})

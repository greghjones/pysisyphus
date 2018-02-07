#!/usr/bin/env python3

import numpy as np

from pysisyphus.helpers import geom_from_library
from pysisyphus.InternalCoordinates import RedundantCoords, DelocalizedCoords
from pysisyphus.calculators.XTB import XTB


np.set_printoptions(suppress=True, precision=4)


def test_fluorethylene():
    # Fluorethylene, see [2] for geometry
    geom = geom_from_library("fluorethylene.xyz")
    forces_fn = "fe_forces"
    #fe_geom.set_calculator(XTB())
    #forces = fe_geom.forces
    #np.savetxt(forces_fn, forces)
    ic = RedundantCoords(geom)
    forces = np.loadtxt(forces_fn)
    #print(forces)
    forces *= 1.0
    step = ic.B_inv.dot(forces)
    #max_step = max(abs(step))
    #if max_step > 0.04:
    #        step /= max_step
    ic.transform(step)
    #assert len(fe_inds) == 5
    #assert len(fe_bends) == 6
    #assert len(fe_dihedrals) == 4


def test_h2o():
    geom = geom_from_library("h2o.xyz")
    forces_fn = "h2o_forces"
    #geom.set_calculator(XTB())
    #forces = geom.forces
    #np.savetxt(forces_fn, forces)
    ic = RedundantCoords(geom)
    forces = np.loadtxt(forces_fn)
    #print(forces)
    forces *= 1#0.2
    step = ic.B_inv.dot(forces)
    #max_step = max(abs(step))
    #if max_step > 0.04:
    #        step /= max_step
    ic.transform(step)
    #assert len(h2o_inds) == 2
    #assert len(h2o_bends) == 1


def run():
    """

    benzene_geom = geom_from_library("benzene_bp86sto3g_opt.xyz")
    benezen_B = get_B_mat(benzene_geom)
    #assert len(benzene_inds) == 12
    """


    """
    # PT H2O
    pt_geom = geom_from_library("h2o_pt.xyz")
    h2o_pt_B = get_B_mat(pt_geom)

    # H2O2, 1 Dihedral
    print("h2o2")
    h2o2_geom = geom_from_library("h2o2_hf_321g_opt.xyz")
    h2o2_B = get_B_mat(h2o2_geom)#, save="h2o2.bmat", tm_format=True)
    """

def test_two_fragments():
    # Two fragments
    print("Two fragments")
    two_frags = geom_from_library("h2o2_h2o_fragments.xyz")
    two_frags_B = get_B_mat(two_frags)

if __name__ == "__main__":
    test_fluorethylene()
    #test_h2o()
    #test_two_fragments()
    #run()

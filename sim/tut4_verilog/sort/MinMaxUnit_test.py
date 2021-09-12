#=========================
# MinMaxUnit_test.py
#=========================

import pytest

from copy              import deepcopy
from random            import randint

from pymtl             import *
from pclib.test        import run_test_vector_sim
from MinMaxUnit        import MinMaxUnit

def test_basic ( dump_vcd ):
    model = MinMaxUnit()
    model.vcd_file = dump_vcd
    model.elaborate()
    
    # Create and reset simulator
    
    sim = SimulationTool(model)
    sim.reset()
    print ""

    def t(in0, in1, out_min, out_max):
        model.in0.value = in0
        model.in1.value = in1
        sim.eval_combinational()
        sim.print_line_trace()
        if (out_min != '?' and out_max != '?'):
            assert model.out_min == out_min
            assert model.out_max == out_max

        sim.cycle()

    t( 0, 1, 0, 1)
    t( 1, 0, 0, 1)

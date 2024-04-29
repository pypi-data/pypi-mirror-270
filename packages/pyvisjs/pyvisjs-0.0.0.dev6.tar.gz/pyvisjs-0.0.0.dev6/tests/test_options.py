from pyvisjs import Options

def test_options_init_default():
    # init

    # mock

    # call
    options = Options()
    
    # assert
    assert options

def test_options_simple_use_case():
    # init
    SCALING_MIN = 10
    SCALING_MAX = 30
    COLOR = "LIME"
    SMOOTH = False
    GR_CONSTANT = -30000
    ST_ITERATIONS = 2500
    OPTIONS_DICT = {
        'width': '100%',
        'height': '100%',
        'edges': {
            'color': COLOR, 
            'smooth': SMOOTH
        }, 
        'nodes': {
            'scaling': {
                'min': SCALING_MIN, 
                'max': SCALING_MAX
            }
        }, 
        'physics': {
            'barnesHut': {'gravitationalConstant': GR_CONSTANT}, 
            'stabilization': {'iterations': ST_ITERATIONS}
        }
    }
    # mock

    # call
    options = Options()
    options.nodes.set_scaling(min = SCALING_MIN, max = SCALING_MAX)
    options.set_edges(color = COLOR, smooth = SMOOTH)
    options.physics.set_barnesHut(gravitationalConstant=GR_CONSTANT)
    options.physics.set_stabilization(iterations=ST_ITERATIONS)
    
    # assert
    assert options.to_dict() == OPTIONS_DICT
"""
Circle Reveal Transition Effect
New image is revealed through an expanding circle from the center
"""

def generate_circle_reveal_transition(prev_img_stream, next_img_stream, transition_duration=1.0):
    """
    Generate FFmpeg filter for circle reveal transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of circle reveal in seconds
    
    Returns:
        String containing FFmpeg filter complex for circle reveal transition
    """
    
    # Create circle reveal effect using mask
    circle_filter = (
        f"color=black:size=1920:1080:duration={transition_duration}:rate=30[base];"
        f"[base]geq=r='if(hypot(X-960,Y-540),if(hypot(X-960,Y-540)<t*600/{transition_duration},255,0),255)':"
        f"g='if(hypot(X-960,Y-540),if(hypot(X-960,Y-540)<t*600/{transition_duration},255,0),255)':"
        f"b='if(hypot(X-960,Y-540),if(hypot(X-960,Y-540)<t*600/{transition_duration},255,0),255)'[mask];"
        f"{prev_img_stream}[mask]alphamerge[masked_prev];"
        f"{next_img_stream}[masked_prev]overlay=0:0[circle_result];"
    )
    
    return circle_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Circular reveal transition where new image appears through an expanding circle from center"

def get_transition_name():
    """Return the name of this transition"""
    return "Circle Reveal"

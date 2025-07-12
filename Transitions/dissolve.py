"""
Dissolve Transition Effect
Creates a smooth dissolve/crossfade between two images
"""

def generate_dissolve_transition(prev_img_stream, next_img_stream, transition_duration=1.0):
    """
    Generate FFmpeg filter for dissolve transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of dissolve transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for dissolve transition
    """
    
    # Create dissolve effect using blend filter with alpha blending
    dissolve_filter = (
        f"{prev_img_stream}fade=t=out:st=0:d={transition_duration}:alpha=1[prev_dissolve];"
        f"{next_img_stream}fade=t=in:st=0:d={transition_duration}:alpha=1[next_dissolve];"
        f"[prev_dissolve][next_dissolve]blend=all_mode=normal:"
        f"all_opacity='1-t/{transition_duration}':enable='lte(t,{transition_duration})'[dissolve_result];"
    )
    
    return dissolve_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Smooth dissolve transition that blends two images together with alpha blending"

def get_transition_name():
    """Return the name of this transition"""
    return "Dissolve"

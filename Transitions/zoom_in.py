"""
Zoom In Transition Effect
Creates a zoom-in effect on the incoming image
"""

def generate_zoom_in_transition(prev_img_stream, next_img_stream, transition_duration=0.8):
    """
    Generate FFmpeg filter for zoom in transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of zoom transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for zoom in transition
    """
    
    # Create zoom in effect - starts small and grows to full size
    zoom_filter = (
        f"{next_img_stream}scale=1920*0.5:1080*0.5,"
        f"zoompan=z='if(lte(zoom,1.0),1.5-0.5*on/{transition_duration*30},1.0)'"
        f":d={int(transition_duration*30)}:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):s=1920x1080[zoomed];"
        f"[zoomed]fade=t=in:st=0:d={transition_duration}[zoom_faded];"
        f"{prev_img_stream}fade=t=out:st=0:d={transition_duration}[prev_faded];"
        f"[prev_faded][zoom_faded]overlay=0:0[zoom_result];"
    )
    
    return zoom_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Dynamic zoom-in effect that makes the new image appear to grow from the center"

def get_transition_name():
    """Return the name of this transition"""
    return "Zoom In"

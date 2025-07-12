"""
Zoom Out Transition Effect
Creates a zoom-out effect on the outgoing image while new image fades in
"""

def generate_zoom_out_transition(prev_img_stream, next_img_stream, transition_duration=0.8):
    """
    Generate FFmpeg filter for zoom out transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of zoom transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for zoom out transition
    """
    
    # Create zoom out effect - previous image zooms out while new image fades in
    zoom_filter = (
        f"{prev_img_stream}zoompan=z='if(lte(zoom,1.0),1.0+0.5*on/{transition_duration*30},1.5)'"
        f":d={int(transition_duration*30)}:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):s=1920x1080[zoomed_out];"
        f"[zoomed_out]fade=t=out:st=0:d={transition_duration}[zoom_out_faded];"
        f"{next_img_stream}fade=t=in:st=0:d={transition_duration}[next_faded];"
        f"[zoom_out_faded][next_faded]overlay=0:0[zoom_out_result];"
    )
    
    return zoom_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Smooth zoom-out effect where the previous image zooms out while the new image fades in"

def get_transition_name():
    """Return the name of this transition"""
    return "Zoom Out"

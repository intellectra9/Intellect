"""
Wipe Transition Effect
New image wipes across from left to right, revealing itself progressively
"""

def generate_wipe_transition(prev_img_stream, next_img_stream, transition_duration=0.8):
    """
    Generate FFmpeg filter for wipe transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of wipe transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for wipe transition
    """
    
    # Create wipe effect - new image progressively reveals itself from left to right
    wipe_filter = (
        f"{next_img_stream}crop=w='t*1920/{transition_duration}':h=1080:x=0:y=0,"
        f"pad=1920:1080:0:0:color=black[wiped];"
        f"{prev_img_stream}[wiped]overlay=0:0:enable='lte(t,{transition_duration})'[wipe_result];"
    )
    
    return wipe_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Progressive wipe transition where new image reveals itself from left to right"

def get_transition_name():
    """Return the name of this transition"""
    return "Wipe"

"""
maix.video module
"""
from __future__ import annotations
import maix._maix.camera
import maix._maix.err
import maix._maix.image
import typing
__all__ = ['Decode', 'Encode', 'Video', 'VideoStream', 'VideoType']
class Decode:
    pass
class Encode:
    pass
class Video:
    def __init__(self, path: str = '', record: bool = False, interval: int = 33333, width: int = -1, height: int = -1, audio: bool = False, sample_rate: int = 44100, channel: int = 1, open: bool = True) -> None:
        ...
    def bind_camera(self, camera: maix._maix.camera.Camera) -> maix._maix.err.Err:
        """
        Bind camera
        
        Args:
          - camera: camera object
        
        
        Returns: error code, err::ERR_NONE means success, others means failed
        """
    def capture(self) -> maix._maix.image.Image:
        """
        stop record video
        
        Returns: error code, err::ERR_NONE means success, others means failed
        """
    def close(self) -> None:
        """
        Close video
        """
    def decode(self, stream: VideoStream) -> maix._maix.image.Image:
        """
        Decode image
        
        Args:
          - img: the image will be decode
        
        
        Returns: decode result
        """
    def encode(self, img: maix._maix.image.Image) -> VideoStream:
        """
        Encode image
        
        Args:
          - img: the image will be encode
        
        
        Returns: encode result
        """
    def height(self) -> int:
        """
        Get video height
        
        Returns: video height
        """
    def is_closed(self) -> bool:
        """
        check video device is closed or not
        
        Returns: closed or not, bool type
        """
    def is_opened(self) -> bool:
        """
        Check if video is opened
        
        Returns: true if video is opened, false if not
        """
    def is_recording(self) -> bool:
        """
        Check if video is recording
        
        Returns: true if video is recording, false if not
        """
    def open(self, path: str = '', record: bool = False, interval: int = 33333, width: int = -1, height: int = -1, audio: bool = False, sample_rate: int = 44100, channel: int = 1) -> maix._maix.err.Err:
        """
        Open video and run
        
        Args:
          - path: video path. if record is true, xxx.h265 means video format is H265, xxx.mp4 means video format is MP4
          - record: If record is true, means record vide. if record is false means play video, default is false.
          - interval: record interval. unit: us
          - width: video width, default is -1, means auto, mostly means max width of video support
          - height: video height, default is -1, means auto, mostly means max height of video support
          - audio: If audio is true, means record with audio. default is false.
          - sample_rate: audio sample rate, default is 44100.
          - channel: audio channel, default is 1.
        
        
        Returns: error code, err::ERR_NONE means success, others means failed
        """
    def record_finish(self) -> maix._maix.err.Err:
        """
        stop record video
        
        Returns: error code, err::ERR_NONE means success, others means failed
        """
    def record_start(self, record_time: int = -1) -> maix._maix.err.Err:
        """
        start record video
        
        Args:
          - record_time: record video time, unit: ms.
        If record_time = -1, mean record will not auto stop until record_finish() is called.
        
        
        Returns: error code, err::ERR_NONE means success, others means failed
        """
    def width(self) -> int:
        """
        Get video width
        
        Returns: video width
        """
class VideoStream:
    pass
class VideoType:
    """
    Members:
    
      VIDEO_NONE
    
      VIDEO_ENC_H265_CBR
    
      VIDEO_ENC_MP4_CBR
    
      VIDEO_DEC_H265_CBR
    
      VIDEO_DEC_MP4_CBR
    """
    VIDEO_DEC_H265_CBR: typing.ClassVar[VideoType]  # value = <VideoType.VIDEO_DEC_H265_CBR: 3>
    VIDEO_DEC_MP4_CBR: typing.ClassVar[VideoType]  # value = <VideoType.VIDEO_DEC_MP4_CBR: 4>
    VIDEO_ENC_H265_CBR: typing.ClassVar[VideoType]  # value = <VideoType.VIDEO_ENC_H265_CBR: 1>
    VIDEO_ENC_MP4_CBR: typing.ClassVar[VideoType]  # value = <VideoType.VIDEO_ENC_MP4_CBR: 2>
    VIDEO_NONE: typing.ClassVar[VideoType]  # value = <VideoType.VIDEO_NONE: 0>
    __members__: typing.ClassVar[dict[str, VideoType]]  # value = {'VIDEO_NONE': <VideoType.VIDEO_NONE: 0>, 'VIDEO_ENC_H265_CBR': <VideoType.VIDEO_ENC_H265_CBR: 1>, 'VIDEO_ENC_MP4_CBR': <VideoType.VIDEO_ENC_MP4_CBR: 2>, 'VIDEO_DEC_H265_CBR': <VideoType.VIDEO_DEC_H265_CBR: 3>, 'VIDEO_DEC_MP4_CBR': <VideoType.VIDEO_DEC_MP4_CBR: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...

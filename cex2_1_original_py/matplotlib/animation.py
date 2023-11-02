# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\animation.pyc
# Compiled at: 2012-11-08 06:38:04
import sys, itertools, contextlib, subprocess
from matplotlib.cbook import iterable, is_string_like
from matplotlib import verbose
from matplotlib import rcParams

class MovieWriterRegistry(object):

    def __init__(self):
        self.avail = dict()

    def register(self, name):

        def wrapper(writerClass):
            if writerClass.isAvailable():
                self.avail[name] = writerClass
            return writerClass

        return wrapper

    def list(self):
        """ Get a list of available MovieWriters."""
        return self.avail.keys()

    def __getitem__(self, name):
        if not self.avail:
            raise RuntimeError('No MovieWriters available!')
        return self.avail[name]


writers = MovieWriterRegistry()

class MovieWriter(object):
    """
    Base class for writing movies. Fundamentally, what a MovieWriter does
    is provide is a way to grab frames by calling grab_frame(). setup()
    is called to start the process and finish() is called afterwards.
    This class is set up to provide for writing movie frame data to a pipe.
    saving() is provided as a context manager to facilitate this process as::

      with moviewriter.saving('myfile.mp4'):
          # Iterate over frames
          moviewriter.grab_frame()

    The use of the context manager ensures that setup and cleanup are
    performed as necessary.

    frame_format: string
        The format used in writing frame data, defaults to 'rgba'
    """

    def __init__(self, fps=5, codec=None, bitrate=None, extra_args=None, metadata=None):
        """
        Construct a new MovieWriter object.

        fps: int
            Framerate for movie.
        codec: string or None, optional
            The codec to use. If None (the default) the setting in the
            rcParam `animation.codec` is used.
        bitrate: int or None, optional
            The bitrate for the saved movie file, which is one way to control
            the output file size and quality. The default value is None,
            which uses the value stored in the rcParam `animation.bitrate`.
            A value of -1 implies that the bitrate should be determined
            automatically by the underlying utility.
        extra_args: list of strings or None
            A list of extra string arguments to be passed to the underlying
            movie utiltiy. The default is None, which passes the additional
            argurments in the 'animation.extra_args' rcParam.
        metadata: dict of string:string or None
            A dictionary of keys and values for metadata to include in the
            output file. Some keys that may be of use include:
            title, artist, genre, subject, copyright, srcform, comment.
        """
        self.fps = fps
        self.frame_format = 'rgba'
        if codec is None:
            self.codec = rcParams['animation.codec']
        else:
            self.codec = codec
        if bitrate is None:
            self.bitrate = rcParams['animation.bitrate']
        else:
            self.bitrate = bitrate
        if extra_args is None:
            self.extra_args = list(rcParams[self.args_key])
        else:
            self.extra_args = extra_args
        if metadata is None:
            self.metadata = dict()
        else:
            self.metadata = metadata
        return

    @property
    def frame_size(self):
        """A tuple (width,height) in pixels of a movie frame."""
        width_inches, height_inches = self.fig.get_size_inches()
        return (width_inches * self.dpi, height_inches * self.dpi)

    def setup(self, fig, outfile, dpi, *args):
        """
        Perform setup for writing the movie file.

        fig: `matplotlib.Figure` instance
            The figure object that contains the information for frames
        outfile: string
            The filename of the resulting movie file
        dpi: int
            The DPI (or resolution) for the file.  This controls the size
            in pixels of the resulting movie file.
        """
        self.outfile = outfile
        self.fig = fig
        self.dpi = dpi
        self._run()

    @contextlib.contextmanager
    def saving(self, *args):
        """
        Context manager to facilitate writing the movie file.

        ``*args`` are any parameters that should be passed to `setup`.
        """
        self.setup(*args)
        yield
        self.finish()

    def _run(self):
        command = self._args()
        if verbose.ge('debug'):
            output = sys.stdout
        else:
            output = subprocess.PIPE
        verbose.report('MovieWriter.run: running command: %s' % (' ').join(command))
        self._proc = subprocess.Popen(command, shell=False, stdout=output, stderr=output, stdin=subprocess.PIPE)

    def finish(self):
        """Finish any processing for writing the movie."""
        self.cleanup()

    def grab_frame(self):
        """
        Grab the image information from the figure and save as a movie frame.
        """
        verbose.report('MovieWriter.grab_frame: Grabbing frame.', level='debug')
        try:
            self.fig.savefig(self._frame_sink(), format=self.frame_format, dpi=self.dpi)
        except RuntimeError:
            out, err = self._proc.communicate()
            verbose.report('MovieWriter -- Error running proc:\n%s\n%s' % (out,
             err), level='helpful')
            raise

    def _frame_sink(self):
        """Returns the place to which frames should be written."""
        return self._proc.stdin

    def _args(self):
        """Assemble list of utility-specific command-line arguments."""
        return NotImplementedError('args needs to be implemented by subclass.')

    def cleanup(self):
        """Clean-up and collect the process used to write the movie file."""
        out, err = self._proc.communicate()
        verbose.report('MovieWriter -- Command stdout:\n%s' % out, level='debug')
        verbose.report('MovieWriter -- Command stderr:\n%s' % err, level='debug')

    @classmethod
    def bin_path(cls):
        """
        Returns the binary path to the commandline tool used by a specific
        subclass. This is a class method so that the tool can be looked for
        before making a particular MovieWriter subclass available.
        """
        return rcParams[cls.exec_key]

    @classmethod
    def isAvailable(cls):
        """
        Check to see if a MovieWriter subclass is actually available by
        running the commandline tool.
        """
        try:
            subprocess.Popen(cls.bin_path(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except OSError:
            return False


class FileMovieWriter(MovieWriter):
    """`MovieWriter` subclass that handles writing to a file."""

    def __init__(self, *args, **kwargs):
        MovieWriter.__init__(self, *args)
        self.frame_format = rcParams['animation.frame_format']

    def setup(self, fig, outfile, dpi, frame_prefix='_tmp', clear_temp=True):
        """
        Perform setup for writing the movie file.

        fig: `matplotlib.Figure` instance
            The figure object that contains the information for frames
        outfile: string
            The filename of the resulting movie file
        dpi: int
            The DPI (or resolution) for the file.  This controls the size
            in pixels of the resulting movie file.
        frame_prefix: string, optional
            The filename prefix to use for the temporary files. Defaults
            to '_tmp'
        clear_temp: bool
            Specifies whether the temporary files should be deleted after
            the movie is written. (Useful for debugging.) Defaults to True.
        """
        self.fig = fig
        self.outfile = outfile
        self.dpi = dpi
        self.clear_temp = clear_temp
        self.temp_prefix = frame_prefix
        self._frame_counter = 0
        self._temp_names = list()
        self.fname_format_str = '%s%%07d.%s'

    @property
    def frame_format(self):
        """
        Format (png, jpeg, etc.) to use for saving the frames, which can be
        decided by the individual subclasses.
        """
        return self._frame_format

    @frame_format.setter
    def frame_format(self, frame_format):
        if frame_format in self.supported_formats:
            self._frame_format = frame_format
        else:
            self._frame_format = self.supported_formats[0]

    def _base_temp_name(self):
        return self.fname_format_str % (self.temp_prefix, self.frame_format)

    def _frame_sink(self):
        fname = self._base_temp_name() % self._frame_counter
        self._temp_names.append(fname)
        verbose.report('FileMovieWriter.frame_sink: saving frame %d to fname=%s' % (
         self._frame_counter, fname), level='debug')
        self._frame_counter += 1
        return open(fname, 'wb')

    def finish(self):
        self._run()
        MovieWriter.finish(self)
        if self._proc.returncode:
            raise RuntimeError('Error creating movie, return code: ' + str(self._proc.returncode) + ' Try running with --verbose-debug')

    def cleanup(self):
        MovieWriter.cleanup(self)
        if self.clear_temp:
            import os
            verbose.report('MovieWriter: clearing temporary fnames=%s' % str(self._temp_names), level='debug')
            for fname in self._temp_names:
                os.remove(fname)


class FFMpegBase():
    exec_key = 'animation.ffmpeg_path'
    args_key = 'animation.ffmpeg_args'

    @property
    def output_args(self):
        args = [
         '-vcodec', self.codec]
        if self.bitrate > 0:
            args.extend(['-b', '%dk' % self.bitrate])
        if self.extra_args:
            args.extend(self.extra_args)
        for k, v in self.metadata.items():
            args.extend(['-metadata', '%s=%s' % (k, v)])

        return args + ['-y', self.outfile]


@writers.register('ffmpeg')
class FFMpegWriter(MovieWriter, FFMpegBase):

    def _args(self):
        args = [
         self.bin_path(), '-f', 'rawvideo', '-vcodec', 'rawvideo',
         '-s', '%dx%d' % self.frame_size, '-pix_fmt', self.frame_format,
         '-r', str(self.fps)]
        if not verbose.ge('debug'):
            args += ['-loglevel', 'quiet']
        args += ['-i', 'pipe:'] + self.output_args
        return args


@writers.register('ffmpeg_file')
class FFMpegFileWriter(FileMovieWriter, FFMpegBase):
    supported_formats = [
     'png', 'jpeg', 'ppm', 'tiff', 'sgi', 'bmp', 
     'pbm', 
     'raw', 'rgba']

    def _args(self):
        return [
         self.bin_path(), '-vframes', str(self._frame_counter),
         '-r', str(self.fps), '-i',
         self._base_temp_name()] + self.output_args


class MencoderBase():
    exec_key = 'animation.mencoder_path'
    args_key = 'animation.mencoder_args'
    allowed_metadata = [
     'name', 'artist', 'genre', 'subject', 'copyright', 
     'srcform', 
     'comment']

    def _remap_metadata(self):
        if 'title' in self.metadata:
            self.metadata['name'] = self.metadata['title']

    @property
    def output_args(self):
        self._remap_metadata()
        args = ['-o', self.outfile, '-ovc', 'lavc', '-lavcopts',
         'vcodec=%s' % self.codec]
        if self.bitrate > 0:
            args.append('vbitrate=%d' % self.bitrate)
        if self.extra_args:
            args.extend(self.extra_args)
        if self.metadata:
            args.extend(['-info',
             (':').join('%s=%s' % (k, v) for k, v in self.metadata.items() if k in self.allowed_metadata)])
        return args


@writers.register('mencoder')
class MencoderWriter(MovieWriter, MencoderBase):

    def _args(self):
        return [
         self.bin_path(), '-', '-demuxer', 'rawvideo', '-rawvideo',
         'w=%i:h=%i:' % self.frame_size + 'fps=%i:format=%s' % (self.fps,
          self.frame_format)] + self.output_args


@writers.register('mencoder_file')
class MencoderFileWriter(FileMovieWriter, MencoderBase):
    supported_formats = [
     'png', 'jpeg', 'tga', 'sgi']

    def _args(self):
        return [
         self.bin_path(),
         'mf://%s*.%s' % (self.temp_prefix, self.frame_format),
         '-frames', str(self._frame_counter), '-mf',
         'type=%s:fps=%d' % (self.frame_format,
          self.fps)] + self.output_args


class Animation(object):
    """
    This class wraps the creation of an animation using matplotlib. It is
    only a base class which should be subclassed to provide needed behavior.

    *fig* is the figure object that is used to get draw, resize, and any
    other needed events.

    *event_source* is a class that can run a callback when desired events
    are generated, as well as be stopped and started. Examples include timers
    (see :class:`TimedAnimation`) and file system notifications.

    *blit* is a boolean that controls whether blitting is used to optimize
    drawing.
    """

    def __init__(self, fig, event_source=None, blit=False):
        self._fig = fig
        self._blit = blit
        self.frame_seq = self.new_frame_seq()
        self.event_source = event_source
        self._init_draw()
        self._first_draw_id = fig.canvas.mpl_connect('draw_event', self._start)
        self._close_id = self._fig.canvas.mpl_connect('close_event', self._stop)
        if blit:
            self._setup_blit()

    def _start(self, *args):
        """
        Starts interactive animation. Adds the draw frame command to the GUI
        handler, calls show to start the event loop.
        """
        self.event_source.add_callback(self._step)
        self.event_source.start()
        self._fig.canvas.mpl_disconnect(self._first_draw_id)
        self._first_draw_id = None
        return

    def _stop(self, *args):
        if self._blit:
            self._fig.canvas.mpl_disconnect(self._resize_id)
        self._fig.canvas.mpl_disconnect(self._close_id)
        self.event_source.remove_callback(self._step)
        self.event_source = None
        return

    def save(self, filename, writer=None, fps=None, dpi=None, codec=None, bitrate=None, extra_args=None, metadata=None, extra_anim=None):
        """
        Saves a movie file by drawing every frame.

        *filename* is the output filename, eg :file:`mymovie.mp4`

        *writer* is either an instance of :class:`MovieWriter` or a string
        key that identifies a class to use, such as 'ffmpeg' or 'mencoder'.
        If nothing is passed, the value of the rcparam `animation.writer` is
        used.

        *fps* is the frames per second in the movie. Defaults to None,
        which will use the animation's specified interval to set the frames
        per second.

        *dpi* controls the dots per inch for the movie frames. This combined
        with the figure's size in inches controls the size of the movie.

        *codec* is the video codec to be used. Not all codecs are supported
        by a given :class:`MovieWriter`. If none is given, this defaults to the
        value specified by the rcparam `animation.codec`.

        *bitrate* specifies the amount of bits used per second in the
        compressed movie, in kilobits per second. A higher number means a
        higher quality movie, but at the cost of increased file size. If no
        value is given, this defaults to the value given by the rcparam
        `animation.bitrate`.

        *extra_args* is a list of extra string arguments to be passed to the
        underlying movie utiltiy. The default is None, which passes the
        additional argurments in the 'animation.extra_args' rcParam.

        *metadata* is a dictionary of keys and values for metadata to include
        in the output file. Some keys that may be of use include:
        title, artist, genre, subject, copyright, srcform, comment.

        *extra_anim* is a list of additional `Animation` objects that should
        be included in the saved movie file. These need to be from the same
        `matplotlib.Figure` instance. Also, animation frames will just be
        simply combined, so there should be a 1:1 correspondence between
        the frames from the different animations.
        """
        if self._first_draw_id is not None:
            self._fig.canvas.mpl_disconnect(self._first_draw_id)
            reconnect_first_draw = True
        else:
            reconnect_first_draw = False
        if fps is None and hasattr(self, '_interval'):
            fps = 1000.0 / self._interval
        if writer is None:
            writer = rcParams['animation.writer']
        if dpi is None:
            dpi = rcParams['savefig.dpi']
        if codec is None:
            codec = rcParams['animation.codec']
        if bitrate is None:
            bitrate = rcParams['animation.bitrate']
        all_anim = [self]
        if extra_anim is not None:
            all_anim.extend(anim for anim in extra_anim if anim._fig is self._fig)
        if is_string_like(writer):
            if writer in writers.avail:
                writer = writers[writer](fps, codec, bitrate, extra_args=extra_args, metadata=metadata)
            else:
                import warnings
                warnings.warn('MovieWriter %s unavailable' % writer)
                writer = writers.list()[0]
        verbose.report('Animation.save using %s' % type(writer), level='helpful')
        with writer.saving(self._fig, filename, dpi):
            for data in itertools.izip(*[ a.new_saved_frame_seq() for a in all_anim ]):
                for anim, d in zip(all_anim, data):
                    anim._draw_next_frame(d, blit=False)

                writer.grab_frame()

        if reconnect_first_draw:
            self._first_draw_id = self._fig.canvas.mpl_connect('draw_event', self._start)
        return

    def _step(self, *args):
        """
        Handler for getting events. By default, gets the next frame in the
        sequence and hands the data off to be drawn.
        """
        try:
            framedata = next(self.frame_seq)
            self._draw_next_frame(framedata, self._blit)
            return True
        except StopIteration:
            return False

    def new_frame_seq(self):
        """Creates a new sequence of frame information."""
        return iter(self._framedata)

    def new_saved_frame_seq(self):
        """Creates a new sequence of saved/cached frame information."""
        return self.new_frame_seq()

    def _draw_next_frame(self, framedata, blit):
        self._pre_draw(framedata, blit)
        self._draw_frame(framedata)
        self._post_draw(framedata, blit)

    def _init_draw(self):
        pass

    def _pre_draw(self, framedata, blit):
        if blit:
            self._blit_clear(self._drawn_artists, self._blit_cache)

    def _draw_frame(self, framedata):
        raise NotImplementedError('Needs to be implemented by subclasses to actually make an animation.')

    def _post_draw(self, framedata, blit):
        if blit and self._drawn_artists:
            self._blit_draw(self._drawn_artists, self._blit_cache)
        else:
            self._fig.canvas.draw_idle()

    def _blit_draw(self, artists, bg_cache):
        updated_ax = []
        for a in artists:
            if a.axes not in bg_cache:
                bg_cache[a.axes] = a.figure.canvas.copy_from_bbox(a.axes.bbox)
            a.axes.draw_artist(a)
            updated_ax.append(a.axes)

        for ax in set(updated_ax):
            ax.figure.canvas.blit(ax.bbox)

    def _blit_clear(self, artists, bg_cache):
        axes = set(a.axes for a in artists)
        for a in axes:
            a.figure.canvas.restore_region(bg_cache[a])

    def _setup_blit(self):
        self._blit_cache = dict()
        self._drawn_artists = []
        self._resize_id = self._fig.canvas.mpl_connect('resize_event', self._handle_resize)
        self._post_draw(None, self._blit)
        return

    def _handle_resize(self, *args):
        self._fig.canvas.mpl_disconnect(self._resize_id)
        self.event_source.stop()
        self._blit_cache.clear()
        self._init_draw()
        self._resize_id = self._fig.canvas.mpl_connect('draw_event', self._end_redraw)

    def _end_redraw(self, evt):
        self._post_draw(None, self._blit)
        self.event_source.start()
        self._fig.canvas.mpl_disconnect(self._resize_id)
        self._resize_id = self._fig.canvas.mpl_connect('resize_event', self._handle_resize)
        return


class TimedAnimation(Animation):
    """
    :class:`Animation` subclass that supports time-based animation, drawing
    a new frame every *interval* milliseconds.

    *repeat* controls whether the animation should repeat when the sequence
    of frames is completed.

    *repeat_delay* optionally adds a delay in milliseconds before repeating
    the animation.
    """

    def __init__(self, fig, interval=200, repeat_delay=None, repeat=True, event_source=None, *args, **kwargs):
        self._interval = interval
        self._repeat_delay = repeat_delay
        self.repeat = repeat
        if event_source is None:
            event_source = fig.canvas.new_timer()
            event_source.interval = self._interval
        Animation.__init__(self, fig, event_source=event_source, *args, **kwargs)
        return

    def _step(self, *args):
        """
        Handler for getting events.
        """
        still_going = Animation._step(self, *args)
        if not still_going and self.repeat:
            self.frame_seq = self.new_frame_seq()
            if self._repeat_delay:
                self.event_source.remove_callback(self._step)
                self.event_source.add_callback(self._loop_delay)
                self.event_source.interval = self._repeat_delay
                return True
            return Animation._step(self, *args)
        else:
            return still_going

    def _stop(self, *args):
        self.event_source.remove_callback(self._loop_delay)
        Animation._stop(self)

    def _loop_delay(self, *args):
        self.event_source.remove_callback(self._loop_delay)
        self.event_source.interval = self._interval
        self.event_source.add_callback(self._step)
        Animation._step(self)


class ArtistAnimation(TimedAnimation):
    """
    Before calling this function, all plotting should have taken place
    and the relevant artists saved.

    frame_info is a list, with each list entry a collection of artists that
    represent what needs to be enabled on each frame. These will be disabled
    for other frames.
    """

    def __init__(self, fig, artists, *args, **kwargs):
        self._drawn_artists = []
        self._framedata = artists
        TimedAnimation.__init__(self, fig, *args, **kwargs)

    def _init_draw(self):
        axes = []
        for f in self.new_frame_seq():
            for artist in f:
                artist.set_visible(False)
                if artist.axes not in axes:
                    axes.append(artist.axes)

        for ax in axes:
            ax.figure.canvas.draw()

    def _pre_draw(self, framedata, blit):
        """
        Clears artists from the last frame.
        """
        if blit:
            self._blit_clear(self._drawn_artists, self._blit_cache)
        else:
            for artist in self._drawn_artists:
                artist.set_visible(False)

    def _draw_frame(self, artists):
        self._drawn_artists = artists
        for artist in artists:
            artist.set_visible(True)


class FuncAnimation(TimedAnimation):
    """
    Makes an animation by repeatedly calling a function *func*, passing in
    (optional) arguments in *fargs*.

    *frames* can be a generator, an iterable, or a number of frames.

    *init_func* is a function used to draw a clear frame. If not given, the
    results of drawing from the first item in the frames sequence will be
    used.
    """

    def __init__(self, fig, func, frames=None, init_func=None, fargs=None, save_count=None, **kwargs):
        if fargs:
            self._args = fargs
        else:
            self._args = ()
        self._func = func
        self.save_count = save_count
        if frames is None:
            self._iter_gen = itertools.count
        elif callable(frames):
            self._iter_gen = frames
        elif iterable(frames):
            self._iter_gen = lambda : iter(frames)
            self.save_count = len(frames)
        else:
            self._iter_gen = lambda : iter(range(frames))
            self.save_count = frames
        if self.save_count is None:
            self.save_count = 100
        self._init_func = init_func
        self._save_seq = []
        TimedAnimation.__init__(self, fig, **kwargs)
        self._save_seq = []
        return

    def new_frame_seq(self):
        return self._iter_gen()

    def new_saved_frame_seq(self):
        if self._save_seq:
            return iter(self._save_seq)
        else:
            return itertools.islice(self.new_frame_seq(), self.save_count)

    def _init_draw(self):
        if self._init_func is None:
            self._draw_frame(next(self.new_frame_seq()))
        else:
            self._drawn_artists = self._init_func()
        return

    def _draw_frame(self, framedata):
        self._save_seq.append(framedata)
        self._save_seq = self._save_seq[-self.save_count:]
        self._drawn_artists = self._func(framedata, *self._args)
import logging
from os import PathLike

from PyQt6 import QtWidgets


def config(filename: str | PathLike[str] | None = "gs-log.log",
           filemode: str = 'a',
           format: str = '%(asctime)s %(levelname)-8s %(message)s',
           datefmt: str | None = '%Y-%m-%d %H:%M:%S',
           level: int | str | None = logging.INFO) -> None:
    """

    :param filename: the name logs will be saved to
    :param filemode: read/write mode for the logfile, 'a' for append
    :param format: how the log will be formatted
    :param datefmt: how the time will be formatted
    :param level: the logging level, default is logging.INFO
    """
    logging.basicConfig(
        filename=filename,
        filemode=filemode,
        format=format,
        level=level,
        datefmt=datefmt,
    )


class LogStreamWidget(logging.Handler):

    def __init__(self, *args, **kwargs):
        """
        A Simple Logging Widget. just use the python standard lib logging and the logs will be displayed in this
        Note: you still need to add Widget as logging handler like the following

        --------------------------------------------------------------------------

        import logging
        star_dresden_gs_lib.components.logs as logs

        logger = logs.LogStreamWidget(self)
        logging.getLogger().addHandler(logger)
        logging.info("test")

        ----------------------------------------------------------------------

        :param args: (optional)
        :param kwargs: (optional)
        """
        super().__init__()
        config()
        self.widget = QtWidgets.QPlainTextEdit()
        self.widget.setStyleSheet("background-color:black; color:white")
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

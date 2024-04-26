"""Loader classes for 1d, 2d, and 3d data - to be used by users."""

# Scientific Modules
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d, interp2d

# Plotting
from bokeh.plotting import show, figure
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper, LogColorMapper, ColorBar, Span, Label, DataRange1d, LinearAxis
from bokeh.io import push_notebook

# Video Export
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

# Utilities
import os
from collections import defaultdict
import io
import shutil
from .util import COLORP, get_emission_line
from .datautil import check_dimensions2d, bokeh_image_boundaries
from .plot_exporter import create_figure, plot_image, plot_lines, save_figure

# Widgets
import ipywidgets as widgets
from IPython.display import display
from ipyfilechooser import FileChooser

# Data processing functions
from .data_1d import load_1d
from .data_2d import load_2d
from .histogram import load_histogram
from .data_3d import load_3d
from .add_subtract import ScanAddition, ScanSubtraction, ImageAddition_2d, ImageSubtraction_2d, ImageAddition_hist, ImageSubtraction_hist, StackAddition, StackSubtraction
from .stitch import ScanStitch, ImageStitch_2d, ImageStitch_hist
from .beamline_info import load_beamline, get_single_beamline_value, get_spreadsheet

#########################################################################################
#########################################################################################


class Load1d:
    """Class to load generic 1d (x,y) data."""

    def __init__(self):
        """Initialize variables and data containers"""
        self.data = list()
        self.legend_loc = 'outside'
        self.plot_vlines = list()
        self.plot_hlines = list()
        self.plot_labels = list()

    def load(self, config, file, x_stream, y_stream, *args, **kwargs):
        """
        Load one or multiple specific scan(s) for selected streams.

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            file name
        x_stream: string
            h5 key or alias of 1d stream
        y_stream: string
            h5 key or alias of 1d, 2d, or 3d stream
        *args: ints
            scans, comma separated
        **kwargs
            norm: boolean
                normalizes to [0,1]
            xoffset: list
                fitting offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list
                fitting offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
            grid_x: list
                grid data evenly with [start,stop,delta]
            savgol: tuple
                (window length, polynomial order, derivative)
            binsize: int
                puts data in bins of specified size
            legend_items: dict
                dict[scan number] = description for legend
            twin_y: boolean
                supports a second y-axis on the right-hand side
            matplotlib_props: dict
                dict[scan number] = dict with props that takes keys:
                    - linewidth
                    - color
                    - linestyle
                    - marker
                    - markersize
                    - etc.
        """

        # Add data index to configuration
        config.index = len(self.data)+1

        # Append all scan objects to scan list in current object.
        self.data.append(load_1d(config, file, x_stream, y_stream, *args, **kwargs))

    def loadObj(self,obj,line):
        """
        Loads data previously specified in a loader

        Parameters
        ----------
        obj: object
            name of the Loader object
        line: int
            Number of the load, add, subtract line (start indexing with 0)
        """

        d = obj.data[line]

        # Overwrite legend index
        index = len(self.data) + 1
        for k,v in d.items():
            d[k].legend = f"{index}-{v.legend}"

        self.data.append(d)

    def background(self,config, file, x_stream, y_stream, *args, **kwargs):
        """ Subtracts the defined data from all loaded data

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            file name
        x_stream: string
            h5 key or alias of 1d stream
        y_stream: string
            h5 key or alias of 1d, 2d, or 3d stream
        *args: int
            scans
        **kwargs
            norm: boolean
                normalizes to [0,1]
            xoffset: list
                fitting offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list
                fitting offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
            grid_x: list
                grid data evenly with [start,stop,delta]
            savgol: tuple
                (window length, polynomial order, derivative)
            binsize: int
                puts data in bins of specified size
            legend_items: dict
                dict[scan number] = description for legend
        """

        # Get the background data
        if len(args) == 1:
            background = load_1d(config, file, x_stream, y_stream, args[0], **kwargs)
            bg_x = background[args[0]].x_stream
            bg_y = background[args[0]].y_stream
        else:
            background = ScanAddition(config, file, x_stream, y_stream, *args, **kwargs)
            bg_x = background[0].x_stream
            bg_y = background[0].y_stream
        
        # Subtract the background from all data objects
        for i, val in enumerate(self.data):
            for k, v in val.items():

                # Determine biggest overlap between background and data
                s = max(v.x_stream.min(),bg_x.min())
                e = min(v.x_stream.max(),bg_x.max())

                x_stream_int = v.x_stream[(v.x_stream>=s) & (v.x_stream<=e)]
                y_stream_int = v.y_stream[(v.x_stream>=s) & (v.x_stream<=e)]

                # Interpolate the background onto the x data
                int_y = interp1d(bg_x,bg_y)(x_stream_int)

                # Remove data
                new_y = np.subtract(y_stream_int,int_y)

                # Overwrite streams in object
                v.x_stream = x_stream_int
                v.y_stream = new_y

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val


    def add(self, config, file, x_stream, y_stream, *args, **kwargs):
        """
        Add specified scans for selected streams.

        Parameters
        ----------
        See loader function.
        Adds all scans specified in *args.
        """

        # Add data index to configuration
        config.index = len(self.data)+1

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ScanAddition(config,
            file, x_stream, y_stream, *args, **kwargs))

    def subtract(self, config, file, x_stream, y_stream, minuend, subtrahend, **kwargs):
        """
        Subtract specified scans for selected streams.

        Parameters
        ----------
        See loader function.
        Subtracts all scans from the first element. May add scans in first element by specifying list of scans as first *arg.
        """

        # Add data index to configuration
        config.index = len(self.data)+1

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ScanSubtraction(config,
            file, x_stream, y_stream, minuend, subtrahend, **kwargs))
        
    def stitch(self, config, file, x_stream, y_stream, *args, **kwargs):
        """
        Stitch specified scans for selected streams.

        Parameters
        ----------
        See loader function.
        Sticthes all scans specified in *args.
        """

        # Add data index to configuration
        config.index = len(self.data)+1

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ScanStitch(config,
            file, x_stream, y_stream, *args, **kwargs))

    def xlim(self, lower, upper):
        """
        Set x-axis limits applied to data stream.

        Parameters
        ----------
        lower : float
        upper : float
        """

        for i, val in enumerate(self.data):
            for k, v in val.items():
                x = v.x_stream
                y = v.y_stream

                # Truncate arrays to limits
                v.x_stream = x[(lower<=x) & (x<=upper)]
                v.y_stream = y[(lower<=x) & (x<=upper)]

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val

    def ylim(self, lower, upper):
        """
        Set y-axis limits applied to data stream.

        Parameters
        ----------
        lower : float
        upper : float
        """

        for i, val in enumerate(self.data):
            for k, v in val.items():
                x = v.x_stream
                y = v.y_stream

                # Truncate arrays to limits
                v.y_stream = y[(lower<=y) & (y<=upper)]
                v.x_stream = x[(lower<=y) & (y<=upper)]

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val

    def plot_legend(self, pos):
        """
        Overwrite default legend position.

        Parameters
        ----------
        pos : string
            See bokeh manual for available options.
        """
        self.legend_loc = pos

    def show_fluorescence(self, element, siegbahn_symbol, orientation='v', **kwargs):
        """
        Draw a line in the plot for the requested fluorescence line.

        Parameters
        ----------
        element: string
            IUPAC element abbreviation
        siegbahn_symbol: string
            Siegbahn symbol for requested energy transition
        orientation: ['v','h']
            Determines if a vertical or horizontal line is drawn
        **kwargs : dict, optional
            See bokeh manual for available options.
        """

        pos = get_emission_line(element, siegbahn_symbol)
        if orientation == 'v':
            self.vline(pos,**kwargs)
        elif orientation == 'h':
            self.hline(pos,**kwargs)
        else:
            raise Exception('Specified line orientation undefined')

    def vline(self, pos, **kwargs):
        """
        Draw a vertical line in the plot.

        Parameters
        ----------
        pos : float
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_vlines.append([pos, kwargs])

    def hline(self, pos, **kwargs):
        """
        Draw a horizontal line in the plot.

        Parameters
        ----------
        pos : float
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_hlines.append([pos, kwargs])

    def label(self, pos_x, pos_y, text, **kwargs):
        """
        Draw a text box in the plot.

        Parameters
        ----------
        pos_x : float
        pos_y : float
        text : string
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_labels.append([pos_x, pos_y, text, kwargs])

    def plot(self, linewidth=4, title=None, xlabel=None, ylabel=None, ylabel_right=None, plot_height=450, plot_width=700, norm=False, waterfall=None, **kwargs):
        """
        Plot all data assosciated with class instance/object.

        Parameters
        ----------
        linewidth : int, optional
        title : string, optional
        xlabel : string, optional
        ylabel : string, optional
        ylabel_right : string, optional
        plot_height : int, optional
        plot_width : int, optional
        norm: boolean, optional
            Normalized plot output to [0,1]
        waterfall: float
            Normalizes plot output to [0,1] and applies offset specified
        kwargs
            all bokeh figure key-word arguments
        """

        # Add a normalization feature to [0,1] for plot only
        if waterfall == None and norm==True:
            waterfall = 0

        # Keep track of 1d x-axis and y-axis labels
            
        xaxis_labels = list()
        yaxis_labels = list()
        yaxis_r_labels = list()

        # Organize all data assosciated with object in sorted dictionary.
        # Separate data by y-axis (if right-hand side axis requested)
        plot_data = defaultdict(list)
        plot_data_twin = defaultdict(list)
        waterfall_i = 0
        waterfall_itwin = 0
        for i, val in enumerate(self.data):
            for k, v in val.items():
                # Check dimensions
                if len(v.x_stream) != len(v.y_stream):
                    raise UserWarning(f'Error in line {i+1}. Cannot plot (x,y) arrays with different size.')
                
                # Track axis labels
                # x
                try:
                    for label in v.xaxis_label:
                        if label not in xaxis_labels:
                            xaxis_labels.append(label)
                except:
                    pass

                # Work on twinned axis
                if hasattr(v,'twin_y'):
                    if v.twin_y != True:

                        # y labels
                        try:
                            for label in v.yaxis_label:
                                if label not in yaxis_labels:
                                    yaxis_labels.append(label)
                        except:
                            pass

                        data_default_dict = plot_data
                        if waterfall == None:
                            y = v.y_stream
                        else:
                            y = waterfall_i*waterfall + np.interp(v.y_stream,(v.y_stream.min(),v.y_stream.max()),(0,1))
                            waterfall_i+=1
                    else:
                        # y label right
                        try:
                            for label in v.yaxis_label:
                                if label not in yaxis_r_labels:
                                    yaxis_r_labels.append(label)
                        except:
                            pass
                        data_default_dict = plot_data_twin
                        if waterfall == None:
                            y = v.y_stream
                        else:
                            y = waterfall_itwin*waterfall + np.interp(v.y_stream,(v.y_stream.min(),v.y_stream.max()),(0,1))
                            waterfall_itwin+=1
                else:

                    # y label
                    try:
                        for label in v.yaxis_label:
                            if label not in yaxis_labels:
                                yaxis_labels.append(label)
                    except:
                        pass

                    data_default_dict = plot_data
                    if waterfall == None:
                        y = v.y_stream
                    else:
                        y = waterfall_i*waterfall + np.interp(v.y_stream,(v.y_stream.min(),v.y_stream.max()),(0,1))
                        waterfall_i+=1

                data_default_dict["x_stream"].append(v.x_stream)
                data_default_dict["y_stream"].append(y)
                data_default_dict['x_name'].append(v.xlabel)
                data_default_dict['y_name'].append(v.ylabel)
                data_default_dict['filename'].append(v.filename)
                data_default_dict['scan'].append(v.scan)
                data_default_dict['legend'].append(v.legend)

        # Get the colours for the glyphs.
        numlines = len(plot_data['scan'])
        plot_data['color'] = COLORP[0:numlines]

        source = ColumnDataSource(plot_data)

        # Set up the bokeh plot
        p = figure(height=plot_height, width=plot_width,
                   tools="pan,wheel_zoom,box_zoom,reset,crosshair,save", **kwargs)
        
        # If twinning enabled, calculate left linear axis and disable default
        # This is because the default axis always scales to maximum range
        if len(plot_data_twin['x_stream']) != 0 and len(plot_data['x_stream']) != 0:
            # Determine the range of the axis and add it to plot
            mins = [min(x) for x in plot_data['y_stream']]
            maxs = [max(x) for x in plot_data['y_stream']]
            yrange = max(maxs)-min(mins)
            ymin = min(mins) - 0.05*yrange
            ymax = max(maxs) + 0.05*yrange

            # Work on labels
            if ylabel != None:
                ystring = str(ylabel)
            else:
                ystring = ""
                for i,label in enumerate(yaxis_labels):
                    if i != 0:
                        ystring+=f"|"
                    ystring+=f"{label}"

            # Disable default axis and add custom axis to left
            p.yaxis.visible = False
            p.extra_y_ranges['left'] = DataRange1d(bounds=(ymin,ymax))
            p.add_layout(LinearAxis(y_range_name='left',axis_label=ystring), 'left')

            default_range = 'left'
        else:
            # Else, main axis remains default
            default_range = 'default'

        # Only try to add plot data to left axis if there is any
        if len(plot_data['x_stream']) != 0:
            p.multi_line(xs='x_stream', ys='y_stream', legend_group="legend",
                        line_width=linewidth, line_color='color', line_alpha=0.6,
                        hover_line_color='color', hover_line_alpha=1.0,
                        source=source,y_range_name=default_range,)
        
        # Plot all data associated with the right side y-axis
        if len(plot_data_twin['x_stream']) != 0:
            # Determine the range of the axis and add it to plot
            mins = [min(x) for x in plot_data_twin['y_stream']]
            maxs = [max(x) for x in plot_data_twin['y_stream']]
            yrange = max(maxs)-min(mins)
            ymin = min(mins) - 0.05*yrange
            ymax = max(maxs) + 0.05*yrange

            # Work on labels
            if ylabel_right != None:
                ystring = ylabel_right
            else:
                ystring = ""
                for i,label in enumerate(yaxis_r_labels):
                    if i != 0:
                        ystring+=f"|"
                    ystring+=f"{label}"

            p.extra_y_ranges['right'] = DataRange1d(bounds=(ymin,ymax))
            p.add_layout(LinearAxis(y_range_name='right',axis_label=ystring), 'right')
            
            # Determine the color
            numlines_y = len(plot_data_twin['scan'])
            plot_data_twin['color'] = COLORP[numlines:numlines+numlines_y]

            # Get the data source
            source_twin = ColumnDataSource(plot_data_twin)
            
            # Add to plot
            p.multi_line(xs='x_stream', ys='y_stream', legend_group="legend",
                     line_width=linewidth, line_color='color', line_alpha=0.6,
                     hover_line_color='color', hover_line_alpha=1.0,
                     source=source_twin,y_range_name='right',)

        # Set up the information for hover box
        p.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[
            ('Scan', '@scan'),
            ('File', '@filename'),
            ("(x,y)", "(@x_name, @y_name)"),
            ("(x,y)", "($x, $y)")
        ]))

        p.toolbar.logo = None

        # Overwrite plot properties if requested.
        if self.legend_loc == 'outside':
            p.add_layout(p.legend[0], 'right')
        else:
            p.legend.location = self.legend_loc

        if len(self.plot_hlines) > 0:
            for line_props in self.plot_hlines:
                line = Span(location=line_props[0],
                            dimension='width', **line_props[1])
                p.add_layout(line)

        if len(self.plot_vlines) > 0:
            for line_props in self.plot_vlines:
                line = Span(
                    location=line_props[0], dimension='height', **line_props[1])
                p.add_layout(line)

        if len(self.plot_labels) > 0:
            for label_props in self.plot_labels:
                label = Label(
                    x=label_props[0], y=label_props[1], text=label_props[2], **label_props[3])
                p.add_layout(label)

        if title != None:
            p.title.text = str(title)
        if xlabel != None:
            p.xaxis.axis_label = str(xlabel)
        else:
            xstring = ""
            for i,label in enumerate(xaxis_labels):
                if i != 0:
                    xstring+=f"|"
                xstring+=f"{label}"
            p.xaxis.axis_label = str(xstring)
        
        if len(plot_data_twin['x_stream']) == 0:
            if ylabel != None:
                p.yaxis.axis_label = str(ylabel)
            else:
                ystring = ""
                for i,label in enumerate(yaxis_labels):
                    if i != 0:
                        ystring+=f"|"
                    ystring+=f"{label}"
                p.yaxis.axis_label = str(ystring)
        show(p)

    def get_data(self):
        """Make data available in memory as exported to file.

        Returns
        -------
        dfT : pandas DataFrame 
            All loaded data.
        files : list
            List of all loaded files.
        """
        
        files = list()
        series_data = list()
        series_header = list()

        # Iterate over all "load" calls
        for i, val in enumerate(self.data):
            # Iterate over all scans per load call.
            for k, v in val.items():
                name = f"~{v.filename}"
                if name not in files:
                    files.append(name)
                fileindex = files.index(name)

                # Append the x_stream data and header name
                series_data.append(pd.Series(v.x_stream))
                series_header.append(f"F{fileindex+1}_S{v.scan}_I{i+1}-{v.xlabel}")

                # Append the y_stream data and header name
                series_data.append(pd.Series(v.y_stream))
                series_header.append(f"F{fileindex+1}_S{v.scan}_I{i+1}-{v.ylabel}")

        dfT = pd.DataFrame(series_data).transpose(copy=True)
        dfT.columns = series_header

        return dfT, files

    def export(self, filename, split_files=False):
        """
        Export and write data to specified file.

        Parameters
        ----------
        filename : string
        split_files: Boolean
            Sets whether scans are exported appended to one file (False), or separately (True)
        """
        dfT, files = self.get_data()

        if split_files == False:

            # Open file.
            with open(f"{filename}.csv", 'w') as f:
                string = '# '
                # Generate list of files for legend.
                for idx, file in enumerate(files):
                    string += f"F{idx+1} {file},"
                string += '\n'
                f.write(string)
                # Write pandas dataframe to file.
                dfT.to_csv(f, index=False, lineterminator='\n')

        else:
            for i in range(0,int(len(dfT.columns)/2)):
                j = i+1
                df2 = dfT[[dfT.columns[2*i],dfT.columns[2*i+1]]]
                df2.to_csv(f'{filename}_{j}.csv',index=False, lineterminator='\n')

        print(f"Successfully wrote DataFrame to {filename}.csv")

    def exporter(self):
        """Interactive exporter widget."""
        current_dir = os.path.dirname(os.path.realpath("__file__"))

        self.exportfile = FileChooser(current_dir)
        self.exportfile.use_dir_icons = True
        #self.exportfile.filter_pattern = '*.csv'

        button = widgets.Button(
            description='Save data file',
            disabled=False,
            button_style='info',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Save data to file',
            icon='save'  # (FontAwesome names without the `fa-` prefix)
        )

        button.on_click(self.exportWidgetStep)
        display(self.exportfile, button)

    def exportWidgetStep(self):
        """Helper function for exporter widget."""
        file = os.path.join(self.exportfile.selected_path,
                            self.exportfile.selected_filename)
        self.export(file)

    def save_plot(self,fname,**kwargs):
        """ Create a matplotlib plot window

            fname: string
                path and file name of the exported file
            kwargs:
                figsize: tuple
                    determines size of plot
                x_minor_ticks: float
                    distance between minor ticks on primary axis
                x_major_ticks: float
                    distance between major ticks on primary axis
                y_minor_ticks: float
                    distance between minor ticks on secondary axis
                y_major_ticks: float
                    distance between major ticks on secondary axis
                top: Boolean
                    Display ticks on top of the plot
                right: Boolean
                    Display ticks on the right of the plot
                fontsize_axes: string or int
                    Set the fontsize of the axes ticks
                fontsize_labels: string or int
                    Set fontsize of the axis labels
                fontsize_title: string or int
                    Set fontsize of the title
                title_pad: int
                    Padding between title and the top of the plot
                xlabel: string
                    Label of the primary axis
                ylabel: string
                    Label of the secondary axis
                title: string
                    Title displayed at the top of the plot
                xlim: tuple
                    Limits the visible x-range
                ylim: tuple
                    Limits the visible y-range
                legend: Boolean
                    Show/Hide plot legend
                fontsize_legend: int
                    Fontsize of the legend entries
                data_format: string, [pdf,svg,png]
                    Sets the output data format and matplotlib backend used
        """

        plot_data_list = list()
        # Iterate over all "load" calls
        for i, val in enumerate(self.data):
            # Iterate over all scans per load call.
            for k, v in val.items():
                data = dict()
                data['x'] = v.x_stream
                data['y'] = v.y_stream
                data['label'] = v.legend
                data['twin_y'] = v.twin_y
                
                data = data | v.matplotlib_props

                plot_data_list.append(data)

        fig,ax = create_figure(**kwargs)
        f = plot_lines(fig,ax,plot_data_list,**kwargs)
        save_figure(f,fname,**kwargs)

#########################################################################################

class Load2d:
    """Class to load generic 2d (x,y,z) image data of a detector."""

    def __init__(self):
        """Initialize variables and data containers"""
        self.data = list()
        self.plot_vlines = list()
        self.plot_hlines = list()
        self.plot_labels = list()

    def load(self, config, file, x_stream, detector, *args, **kwargs):
        """
        Load one or multiple specific scan(s) for selected streams.

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            filename
        x_stream: string
            h5 sca key or alias of the x-stream
        detector: string
            alias of the MCA detector
        arg: int
            scan number
        **kwargs
            norm: boolean
                Can be boolean or None (as False)
            xoffset: list of tuples
                fitted offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list of tuples
                fitted offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
            grid_x: list
                grid equally spaced in x with [start, stop, delta]
            grid_y: list
                grid equally spaced in y with [start, stop, delta]
            norm_by: string
                norm MCA by defined h5 key or SCA alias
            binsize_x: int
                puts data in bins of specified size in the horizontal direction
            binsize: int
                puts data in bins of specified size in the vertical direction
        """

        # Ensure that only one scan is loaded.
        if len(args) != 1:
            raise TypeError("You may only select one scan at a time")
        if self.data != []:
            raise TypeError("You can only append one scan per object")
        
        self.data.append(load_2d(config, file, x_stream, detector, *args, **kwargs))

    def background_1d(self,config, file, x_stream, y_stream, *args, axis='y', **kwargs):
        """ Subtracts the defined data from all loaded data

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            file name
        x_stream: string
            h5 key or alias of 1d stream
        y_stream: string
            h5 key or alias of 1d stream
        *args: int
            scans
        **kwargs
            axis: string
                <<x>> or <<y>> axis for subtraction direction
            norm: boolean
                normalizes to [0,1]
            xoffset: list
                fitting offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list
                fitting offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
            grid_x: list
                grid data evenly with [start,stop,delta]
            savgol: tuple
                (window length, polynomial order, derivative)
            binsize: int
                puts data in bins of specified size
            legend_items: dict
                dict[scan number] = description for legend
        """

        # Get the background data
        if len(args) == 1:
            background = load_1d(config, file, x_stream, y_stream, args[0], **kwargs)
            bg_x = background[args[0]].x_stream
            bg_y = background[args[0]].y_stream
        else:
            background = ScanAddition(config, file, x_stream, y_stream, *args, **kwargs)
            bg_x = background[0].x_stream
            bg_y = background[0].y_stream

        if axis == 'y':
            # Subtract the background from all data objects
            for i, val in enumerate(self.data):
                for k, v in val.items():

                    # Determine biggest overlap between background and data
                    s = max(v.new_y.min(),bg_x.min())
                    e = min(v.new_y.max(),bg_x.max())
                    d = np.diff(v.new_y).min()
                    ds = int((e-s)/d)+1
                    new_y = np.linspace(s,e,ds)
                    
                    # Interpolate background and generate 2d array
                    img_int = interp2d(v.new_x,v.new_y,v.new_z)(v.new_x,new_y)
                    arr_subtract = interp1d(bg_x,bg_y)(new_y)
                    img_subtract = np.transpose(np.repeat(arr_subtract[None,...],len(v.new_x),axis=0))
                    
                    # Remove data
                    new_z = np.subtract(img_int,img_subtract)

                    # Overwrite streams in object
                    v.new_y = new_y
                    v.new_z = new_z
                    
                    # Update dictionary with new object
                    val[k] = v

                # Update data list with updated dictionary
                self.data[i] = val

        elif axis == 'x':
            # Subtract the background from all data objects
            for i, val in enumerate(self.data):
                for k, v in val.items():
                    # Determine biggest overlap between background and data
                    s = max(v.new_x.min(),bg_x.min())
                    e = min(v.new_x.max(),bg_x.max())
                    d = np.diff(v.new_x).min()
                    ds = int((e-s)/d)+1
                    new_x = np.linspace(s,e,ds)
                    
                    # Interpolate background and generate 2d array
                    img_int = interp2d(v.new_x,v.new_y,v.new_z)(new_x,v.new_y)
                    arr_subtract = interp1d(bg_x,bg_y)(new_x)
                    img_subtract = np.repeat(arr_subtract[None,...],len(v.new_y),axis=0)
                    
                    # Remove data
                    new_z = np.subtract(img_int,img_subtract)

                    # Overwrite streams in object
                    v.new_x = new_x
                    v.new_z = new_z
                    
                    # Update dictionary with new object
                    val[k] = v

                # Update data list with updated dictionary
                self.data[i] = val

        else:
            raise Exception(f"Specified axis {axis} unknown.")
        
    def background_2d(self,config, file, x_stream, detector, *args, **kwargs):
        """ Subtracts the defined data from all loaded data

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            file name
        x_stream: string
            h5 key or alias of 1d stream
        detector: string
            alias of the MCA detector
        *args: int
            scans
        **kwargs
            norm: boolean
                normalizes to [0,1]
            xoffset: list
                fitting offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list
                fitting offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
            grid_x: list
                grid data evenly with [start,stop,delta]
            savgol: tuple
                (window length, polynomial order, derivative)
            binsize: int
                puts data in bins of specified size
            legend_items: dict
                dict[scan number] = description for legend
            binsize_x: int
                puts data in bins of specified size in the horizontal direction
            binsize: int
                puts data in bins of specified size in the vertical direction
        """

        # Get the background data
        if len(args) == 1:
            background = load_2d(config, file, x_stream, detector, args[0], **kwargs)
            bg_x = background[args[0]].new_x
            bg_y = background[args[0]].new_y
            bg_z = background[args[0]].new_z
        else:
            background = ImageAddition_2d(config,file, x_stream, detector, *args, **kwargs)
            bg_x = background[0].new_x
            bg_y = background[0].new_y
            bg_z = background[0].new_z
        
        # Subtract the background from all data objects
        for i, val in enumerate(self.data):
            for k, v in val.items():
                # Determine biggest overlap between background and data
                s_x = max(v.new_x.min(),bg_x.min())
                e_x = min(v.new_x.max(),bg_x.max())
                d_x = np.diff(v.new_x).min()
                ds_x = int((e_x-s_x)/d_x)+1
                s_y = max(v.new_y.min(),bg_y.min())
                e_y = min(v.new_y.max(),bg_y.max())
                d_y = np.diff(v.new_y).min()
                ds_y = int((e_y-s_y)/d_y)+1

                new_x = np.linspace(s_x,e_x,ds_x)
                new_y = np.linspace(s_y,e_y,ds_y)

                # Interpolate the x,y data onto the background
                bg_z_int = interp2d(bg_x,bg_y,bg_z)(new_x,new_y)
                im_z_int = interp2d(v.new_x,v.new_y,v.new_z)(new_x,new_y)

                # Remove data
                new_z = np.subtract(im_z_int,bg_z_int)

                # Overwrite streams in object
                v.new_x = new_x
                v.new_y = new_y
                v.new_z = new_z

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val

    def add(self, config, file, x_stream, detector, *args, **kwargs):
        """
        Add specified images for selected streams.

        Parameters
        ----------
        See loader function.
        Adds all scans specified in *args.
        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")

        self.data.append(ImageAddition_2d(config,file, x_stream,
                         detector, *args, **kwargs))
        

    def subtract(self, config, file, x_stream, detector, *args, **kwargs):
        """
        Subtract specified images for selected streams.

        Parameters
        ----------
        See loader function.
        Subtracts all imnages from the first element.

        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ImageSubtraction_2d(config, file, x_stream,
                         detector, *args, **kwargs))
        
    def stitch(self, config, file, x_stream, detector, *args, **kwargs):
        """
        Stitch specified scans for selected image.

        Parameters
        ----------
        See loader function.
        Sticthes all scans specified in *args.
        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ImageStitch_2d(config,
            file, x_stream, detector, *args, **kwargs))
        

    def xlim(self, lower, upper):
        """
        Set x-axis limits applied to data stream.

        Parameters
        ----------
        lower : float
        upper : float
        """

        for i, val in enumerate(self.data):
            for k, v in val.items():
                x = v.new_x
                z = v.new_z

                # Truncate arrays to limits
                v.new_x = x[(lower<=x) & (x<=upper)]
                v.new_z = z[:,np.where((lower<=x) & (x<=upper))[0]]

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val

    def ylim(self, lower, upper):
        """
        Set y-axis limits applied to data stream.

        Parameters
        ----------
        lower : float
        upper : float
        """
        
        for i, val in enumerate(self.data):
            for k, v in val.items():
                y = v.new_y
                z = v.new_z

                # Truncate arrays to limits
                v.new_y = y[(lower<=y) & (y<=upper)]
                v.new_z = z[np.where((lower<=y) & (y<=upper))[0],:]

                # Update dictionary with new object
                val[k] = v

            # Update data list with updated dictionary
            self.data[i] = val

    def show_fluorescence(self, element, siegbahn_symbol, orientation='v', **kwargs):
        """
        Draw a line in the plot for the requested fluorescence line.

        Parameters
        ----------
        element: string
            IUPAC element abbreviation
        siegbahn_symbol: string
            Siegbahn symbol for requested energy transition
        orientation: ['v','h']
            Determines if a vertical or horizontal line is drawn
        **kwargs : dict, optional
            See bokeh manual for available options.
        """

        pos = get_emission_line(element, siegbahn_symbol)
        if orientation == 'v':
            self.vline(pos,**kwargs)
        elif orientation == 'h':
            self.hline(pos,**kwargs)
        else:
            raise Exception('Specified line orientation undefined')

    def vline(self, pos, **kwargs):
        """
        Draw a vertical line in the plot.

        Parameters
        ----------
        pos : float
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_vlines.append([pos, kwargs])

    def hline(self, pos, **kwargs):
        """
        Draw a horizontal line in the plot.

        Parameters
        ----------
        pos : float
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_hlines.append([pos, kwargs])

    def label(self, pos_x, pos_y, text, **kwargs):
        """
        Draw a text box in the plot.

        Parameters
        ----------
        pos_x : float
        pos_y : float
        text : string
        **kwargs : dict, optional
            See bokeh manual for available options.
        """
        self.plot_labels.append([pos_x, pos_y, text, kwargs])

    def plot(self, title=None, kind='Image', xlabel=None, ylabel=None, zlabel=None, plot_height=600, plot_width=600, 
            vmin=None, vmax=None, colormap = "linear", norm=False, **kwargs):
        """
        Plot all data assosciated with class instance/object.

        Parameters
        ----------
        title : string, optional
        kind : string, optional
        xlabel : string, optional
        ylabel : string, optional
        zlabel : string, optional
        plot_height : int, optional
        plot_width : int, optional
        vmin : float, optional
        vmax : float, optional
        colormap : string
            Use: "linear" or "log"
        norm : boolean
            to normalize the plot to the maximum
        kwargs
            all bokeh figure key-word arguments
        """
        # Iterate over the one (1) scan in object - this is for legacy reason and shall be removed in the future.
        for i, val in enumerate(self.data):
            for k, v in val.items():

                # Let's ensure dimensions are matching
                check_dimensions2d(v.new_x,v.new_y,v.new_z)

                # Check if normalizing the plot is requested
                if norm==True:
                    v.new_z = v.new_z/np.max(v.new_z)

                # Create the figure
                p = figure(height=plot_height, width=plot_width, tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")],
                           tools="pan,wheel_zoom,box_zoom,reset,hover,crosshair,save", **kwargs)
                p.x_range.range_padding = p.y_range.range_padding = 0

                # must give a vector of image data for image parameter
                if vmin == None:
                    mapper_low = v.new_z.min()
                else:
                    mapper_low = vmin

                if vmax == None:
                    mapper_high = v.new_z.max()
                else:
                    mapper_high = vmax

                if colormap == "linear":
                    myMapper = LinearColorMapper
                elif colormap == "log":
                    myMapper = LogColorMapper
                else:
                    raise UserWarning("Only 'linear' and 'log' implemented.")

                color_mapper = myMapper(palette="Viridis256",
                                                 low=mapper_low,
                                                 high=mapper_high)

                # Calculate boundaries and shape of image for plotter
                # so that pixels are centred at their given values
                # since bokeh takes the left bound of the first and right bound of the last pixel
                plot_x_corner,plot_y_corner, plot_dw,plot_dh = bokeh_image_boundaries(v.new_x,v.new_y)

                # Plot image and use limits as given by even grid.
                p.image(image=[v.new_z], x=plot_x_corner, y=plot_y_corner, dw=plot_dw,
                        dh=plot_dh, color_mapper=color_mapper, level="image")
                p.grid.grid_line_width = 0.5

                # Defining properties of color mapper
                if zlabel == None:
                    zstring = 'Counts'
                else:
                    zstring = zlabel
                color_bar = ColorBar(color_mapper=color_mapper,
                                     label_standoff=12,
                                     location=(0, 0),
                                     title=zstring)
                p.add_layout(color_bar, 'right')

                # Overwrite plot properties if selected.

                if len(self.plot_hlines) > 0:
                    for line_props in self.plot_hlines:
                        line = Span(
                            location=line_props[0], dimension='width', **line_props[1])
                        p.add_layout(line)

                if len(self.plot_vlines) > 0:
                    for line_props in self.plot_vlines:
                        line = Span(
                            location=line_props[0], dimension='height', **line_props[1])
                        p.add_layout(line)

                if len(self.plot_labels) > 0:
                    for label_props in self.plot_labels:
                        label = Label(
                            x=label_props[0], y=label_props[1], text=label_props[2], **label_props[3])
                        p.add_layout(label)

            if title != None:
                p.title.text = str(title)
            else:
                p.title.text = f'{v.zlabel} {kind} for Scan {v.scan}'
            if xlabel != None:
                p.xaxis.axis_label = str(xlabel)
            else:
                p.xaxis.axis_label = str(v.xlabel)
            if ylabel != None:
                p.yaxis.axis_label = str(ylabel)
            else:
                p.yaxis.axis_label = str(v.ylabel)

            p.toolbar.logo = None

            show(p)

    def get_data(self):
        """Make data available in memory as exported to file.

        Returns
        -------
        f : string.IO object
            Motor and Detector Scales. Pandas Data Series.
            1) Rewind memory with f.seek(0)
            2) Load with pandas.read_csv(f,skiprows=3)
        g : string.IO object
            Actual gridded detector image.
            1) Rewind memory with g.seek(0)
            2) Load with numpy.genfromtxt(g,skip_header=4)
        raw_data: list
            List of lists with series data, series header, and matrix_data
        """
        # Set up the data frame and the two string objects for export
        f = io.StringIO()
        g = io.StringIO()
        series_data = list()
        series_header = list()
        matrix_data = list()

        for i, val in enumerate(self.data):
            for k, v in val.items():
                # Gridded scales now calculated directly during the MCA load and only need to be referenced here

                # Start writing string f
                f.write("========================\n")
                f.write(
                    f"F~{v.filename}_S{v.scan}_{v.zlabel}_{v.xlabel}_{v.ylabel}\n")
                f.write("========================\n")

                # Start writing string g
                g.write("========================\n")
                g.write(
                    f"F~{v.filename}_S{v.scan}_{v.zlabel}_{v.xlabel}_{v.ylabel}\n")
                g.write("========================\n")

                # Append data to string now.
                # Append x-stream
                series_data.append(pd.Series(v.new_x))
                series_header.append(f"{v.xlabel} Gridded")

                # Append y-stream
                series_data.append(pd.Series(v.new_y))
                series_header.append(f"{v.ylabel} Gridded")

                dfT = pd.DataFrame(series_data).transpose(copy=True)
                dfT.columns = series_header
                dfT.to_csv(f, index=False, lineterminator='\n')

                g.write(f"=== {v.zlabel} ===\n")
                np.savetxt(g, v.new_z, fmt="%.9g")
                matrix_data.append(v.new_z)

            
        raw_data = [series_data,series_header,matrix_data]

        return f, g, raw_data

    def export(self, filename, split_files=False):
        """
        Export and write data to specified file.

        Parameters
        ----------
        filename : string
        split_files: Boolean
            Sets whether scans are exported appended to one file (False), or separately (True)
        """
        f, g, raw_data = self.get_data()

        if split_files == False:
            # Dump both strings in file.
            # Need to rewind memory location of String.IO to move to beginning.
            # Copy string content to file with shutil.
            with open(f"{filename}.txt_scale", "a") as scales:
                f.seek(0)
                shutil.copyfileobj(f, scales)

            with open(f"{filename}.txt_matrix", "a") as matrix:
                g.seek(0)
                shutil.copyfileobj(g, matrix)

        else:
            # iterate over matrices
            for i,m in enumerate(raw_data[2]):
                j = i+1
                np.savetxt(f"{filename}_{j}.txt_matrix", m)
                np.savetxt(f"{filename}_{j}.txt_scale1", raw_data[0][2*i],header=raw_data[1][2*i])
                np.savetxt(f"{filename}_{j}.txt_scale2", raw_data[0][2*i+1],header=raw_data[1][2*i+1])

        print(f"Successfully wrote Image data to {filename}.txt")

    def exporter(self):
        """Interactive exporter widget."""
        current_dir = os.path.dirname(os.path.realpath("__file__"))

        self.exportfile = FileChooser(current_dir)
        self.exportfile.use_dir_icons = True
        #self.exportfile.filter_pattern = '*.txt'

        button = widgets.Button(
            description='Save data file',
            disabled=False,
            button_style='info',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Save data to file',
            icon='save'  # (FontAwesome names without the `fa-` prefix)
        )

        button.on_click(self.exportWidgetStep)
        display(self.exportfile, button)

    def exportWidgetStep(self):
        """Helper function for exporter widget."""
        file = os.path.join(self.exportfile.selected_path,
                            self.exportfile.selected_filename)
        self.export(file)

    def save_plot(self,fname,**kwargs):
        """ Create a matplotlib plot window

            fname: string
                path and file name of the exported file
            kwargs:
                figsize: tuple
                    determines size of plot
                x_minor_ticks: float
                    distance between minor ticks on primary axis
                x_major_ticks: float
                    distance between major ticks on primary axis
                y_minor_ticks: float
                    distance between minor ticks on secondary axis
                y_major_ticks: float
                    distance between major ticks on secondary axis
                top: Boolean
                    Display ticks on top of the plot
                right: Boolean
                    Display ticks on the right of the plot
                fontsize_axes: string or int
                    Set the fontsize of the axes ticks
                fontsize_labels: string or int
                    Set fontsize of the axis labels
                fontsize_title: string or int
                    Set fontsize of the title
                title_pad: int
                    Padding between title and the top of the plot
                xlabel: string
                    Label of the primary axis
                ylabel: string
                    Label of the secondary axis
                title: string
                    Title displayed at the top of the plot
                xlim: tuple
                    Limits the visible x-range
                ylim: tuple
                    Limits the visible y-range
                cmap: string
                    name of matplotlib colourmap
                levels: int
                    determines how many levels the z data should be binned in
                aspect: [equal, auto]
                    Set the axis to scale or stretch figszize
                colorbar: Boolean
                    Display a colorbar
                zlabel: string
                    Label of the colorbar
                fontsize_colorbar: string or int
                    Fontsize of the colorbar ticks
                data_format: string, [pdf,svg,png]
                    Sets the output data format and matplotlib backend used
        """

        for i, val in enumerate(self.data):
            for k, v in val.items():
                fig,ax = create_figure(**kwargs)
                fig = plot_image(fig,ax,v.new_x,v.new_y,v.new_z,**kwargs)
                if i == 0:
                    save_figure(fig,fname,**kwargs)
                else:
                    save_figure(fig,f"{fname}_i",**kwargs)


#########################################################################################

class LoadHistogram(Load2d):
    """Class to display (x,y,z) scatter data."""

    def load(self, config, file, x_stream, y_stream, z_stream, *args, **kwargs):
        """
        Load (x,y,z) stream data to histogram

        Parameters
        ----------
        config: dict
            h5 configuration
        file: string
            file name
        x_stream: string
            key name or alias
        y_stream: string
            key name or alias
        z_stream: string
            key name or alias
        args: int
            scan number
        kwargs:
            norm: boolean
                normalizes to [0,1]
            xoffset: list
                fitting offset (x-stream)
            xcoffset: float
                constant offset (x-stream)
            yoffset: list
                fitting offset (y-stream)
            ycoffset: float
                constant offset (y-stream)
        """
        
        # Ensure that only one scan is loaded.
        if len(args) != 1:
            raise TypeError("You may only select one scan at a time")
        if self.data != []:
            raise TypeError("You can only append one scan per object")
        
        self.data.append(load_histogram(config, file, x_stream,
                         y_stream, z_stream, *args, **kwargs))

    def add(self, config, file, x_stream, y_stream, z_stream, *args, **kwargs):
        """
        Add specified histograms for selected streams.

        Parameters
        ----------
        See loader function.
        Adds all scans specified in *args.
        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")
        
        self.data.append(ImageAddition_hist(config, file, x_stream,
                         y_stream, z_stream, *args, **kwargs))
    
    def subtract(self, config, file, x_stream, y_stream, z_stream, *args, **kwargs):
        """
        Subract specified histograms for selected streams.

        Parameters
        ----------
        See loader function.
        Subtracts all scans specified in two *args lists.
        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")
        
        self.data.append(ImageSubtraction_hist(config, file, x_stream,
                         y_stream, z_stream, *args, **kwargs))
        

    def stitch(self, config, file, x_stream, y_stream, z_stream, *args, **kwargs):
        """
        Stitch specified scans for selected histograms.

        Parameters
        ----------
        See loader function.
        Sticthes all scans specified in *args.
        """

        # Ensure that only one scan is loaded.
        if self.data != []:
            raise TypeError("You can only append one scan per object")

        # Append all REIXS scan objects to scan list in current object.
        self.data.append(ImageStitch_hist(config, file, x_stream, y_stream, z_stream, *args, **kwargs))


    def plot(self, *args, **kwargs):
        kwargs.setdefault('kind', "Histogram")

        super().plot(*args, **kwargs)

#########################################################################################
        
class Load3d:
    """Object to hold a 3d stack of images"""

    def __init__(self):
        """Initialize variables and data containers"""
        self.data = list()

    def load(self, config, file, ind_stream, stack, arg,**kwargs):
        """ Shows a 3d stack of images interactively

            Parameters
            ----------
            config: dict
                h5 configuration
            file: string
                filename
            ind_stream: string
                independent stream, corresponding to stack's first dim
            stack: string
                alias of an image STACK
            args: int
                scan number
            kwargs
                xoffset: list of tuples
                    fitted offset (x-stream)
                xcoffset: float
                    constant offset (x-stream)
                yoffset: list of tuples
                    fitted offset (y-stream)
                ycoffset: float
                    constant offset (y-stream)
                grid_x: list
                    grid equally spaced in x with [start, stop, delta]
                grid_y: list
                    grid equally spaced in y with [start, stop, delta]
                norm_by: string
                    norm MCA by defined h5 key or SCA alias
        """

        # Ensure we only load 1
        if self.data != []:
            raise UserWarning("Can only load one movie at a time.")
        else:
            self.data.append(load_3d(config, file, ind_stream, stack, arg, **kwargs))

    def add(self, config, file, ind_stream, stack, *args,**kwargs):
        """ Adds 3d stacks of images with identical scales

            Parameters
            ----------
            See Load3d function.
            Adds all scans specified in *args.
        """

        # Ensure we only load 1
        if self.data != []:
            raise UserWarning("Can only load one movie at a time.")
        else:
            self.data.append(StackAddition(config, file, ind_stream, stack, *args, **kwargs))


    def subtract(self, config, file, ind_stream, stack, minuend, subtrahend,**kwargs):
        """ Subtracts 3d stacks of images with identical scales

            Parameters
            ----------
            See Load3d function, but
            minuend: list
                adds all images in list, generates minuend
            subtrahend: list
                adds all images in list, generates subtrahend
        """

        # Ensure we only load 1
        if self.data != []:
            raise UserWarning("Can only load one movie at a time.")
        else:
            self.data.append(StackSubtraction(config, file, ind_stream, stack, minuend, subtrahend, **kwargs))


    def plot(self, title=None, xlabel=None, ylabel=None, plot_height=600, plot_width=600, norm=False, **kwargs):
        """
        Plot all data assosciated with class instance/object.

        Parameters
        ----------
        title : string, optional
        xlabel : string, optional
        ylabel : string, optional
        plot_height : int, optional
        plot_width : int, optional
        norm: boolean
            Normalizes to the maximum z-value across all images in the stack
        kwargs
            all bokeh figure key-word arguments
        """

        def update(g='init'):
            """Update stack to next image on slider move"""

            if g == 'init':
                f = 0
            else:
                f = indices[g['new']]
                
            # This is for sanity check
            # Let's ensure dimensions are matching
            check_dimensions2d(v.new_x[f],v.new_y[f],v.stack[f])

            # Get data
            plot_x_corner,plot_y_corner, plot_dw,plot_dh = bokeh_image_boundaries(v.new_x[f],v.new_y[f])

            # This is to update bokeh data
            if norm == True:
                r.data_source.data['image'] = [v.stack[f]/np.max(v.stack)]
            else:
                r.data_source.data['image'] = [v.stack[f]]
            r.data_source.data['x'] = [plot_x_corner]
            r.data_source.data['y'] = [plot_y_corner]
            r.data_source.data['dw'] = [plot_dw]
            r.data_source.data['dh'] = [plot_dh]

            push_notebook(handle=s)

        for i, val in enumerate(self.data):
            for k, v in val.items():

                # Map values of independent stream to indices
                indices = {k: v for v,k in enumerate(v.ind_stream)}

                # Let's ensure dimensions are matching
                check_dimensions2d(v.new_x[0],v.new_y[0],v.stack[0])

                p = figure(height=plot_height, width=plot_width, tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")],
                           tools="pan,wheel_zoom,box_zoom,reset,hover,crosshair,save",**kwargs)
                p.x_range.range_padding = p.y_range.range_padding = 0

                # must give a vector of image data for image parameter
                color_mapper = LinearColorMapper(palette="Viridis256")

                # Calculate boundaries and shape of image for plotter
                # so that pixels are centred at their given values
                # since bokeh takes the left bound of the first and right bound of the last pixel
                plot_x_corner,plot_y_corner, plot_dw,plot_dh = bokeh_image_boundaries(v.new_x[0],v.new_y[0])

                if norm==True:
                    init_img = v.stack[0] / np.max(v.stack)
                else:
                    init_img = v.stack[0]

                simage = ColumnDataSource(data=dict(image=[init_img], x=[plot_x_corner], y=[
                                          plot_y_corner], dw=[plot_dw], dh=[plot_dh],))

                r = p.image(image='image', source=simage, x='x', y='y',
                            dw='dw', dh='dh', color_mapper=color_mapper, level="image")
                p.grid.grid_line_width = 0.5

                # Defining properties of color mapper
                color_bar = ColorBar(color_mapper=color_mapper,
                                     label_standoff=12,
                                     location=(0, 0),
                                     title='Counts')
                p.add_layout(color_bar, 'right')

                p.toolbar.logo = None

                if title != None:
                    p.title.text = str(title)
                else:
                    p.title.text = f'Image Stack Movie for Scan {k}'
                if xlabel != None:
                    p.xaxis.axis_label = str(xlabel)
                else:
                    p.xaxis.axis_label = str(v.xlabel)
                if ylabel != None:
                    p.yaxis.axis_label = str(ylabel)
                else:
                    p.yaxis.axis_label = str(v.ylabel)

                s = show(p, notebook_handle=True)

                # create SelectionSlider
                mywidget = widgets.SelectionSlider(
                options=v.ind_stream,
                value=v.ind_stream[0],
                description=v.str_ind_stream,
                disabled=False,
                continuous_update=True,
                orientation='horizontal',
                readout=True
            )
                
                # Hook-up widget to update function, then display
                mywidget.observe(update,names='value')
                display(mywidget)

    def export(self,filename, interval=500, aspect=1, xlim=None, ylim=None, **kwargs):
        """ Export Stack image as movie

            Parameters
            ----------
            filename: string
            interval: int
                duration of each frame in ms
            aspect: float
                aspect ratio
            xlim: None, tuple
            ylim: None, tuple
            kwargs
                all matplotlib figure key-word arguments
        """

        for i, val in enumerate(self.data):
            for k, v in val.items():
                frames = list()
                fig  = plt.figure(**kwargs)
                if not isinstance(xlim,type(None)):
                    plt.xlim(xlim)
                if not isinstance(ylim,type(None)):
                    plt.ylim(ylim)
                for i,img in enumerate(v.stack):
                    frames.append([plt.imshow(img,animated=True,extent=[v.new_x[i].min(),v.new_x[i].max(),v.new_y[i].min(),v.new_y[i].max()],aspect=aspect)])
            
                ani = animation.ArtistAnimation(fig, frames, interval=interval, blit=True,
                                repeat_delay=10000)
                ani.save(filename+'.mp4')

#########################################################################################
class LoadBeamline(Load1d):
    """Load meta data as 1d data stream."""
    def load(self, config, file, key, **kwargs):
        """
        Load one or multiple specific scan(s) for selected streams.

        Parameters
        ----------
        basedir : string
            Specifiy the absolute or relative path to experimental data.
        file : string
            Specify the file name (either ASCII or HDF5).
        key : string
        **kwargs: multiple, optional
            Options:
                average: Boolean
                    determines if array of values or their average is reported
                norm : boolean
                    Norm the spectra to [0,1].
                    default: True
                xoffset : list of tuples
                    Offset the x-axis by applying a polynomial fit.
                    default: None
                xcoffset : float
                    Offset x-axis by constant value.
                    default : None 
                yoffset : list of tuples
                    Offset the y-axis by applying a polynomial fit.
                    default : None 
                ycoffset : float
                    Offset y-axis by constant value.
                    default : None
        """

        # Add data index to configuration
        config.index = len(self.data)+1

        # Append all scan objects to scan list in current object.
        self.data.append(load_beamline(config, file, key, **kwargs))

    def add(*args):
        raise UserWarning('Undefined')

    def subtract(*args):
        raise UserWarning('Undefined')

#########################################################################################

class LoadLog:
    """Generate spreadsheet with meta data from h5 file."""
    def __init__(self):
        """Initialize variables and data containers"""
        pass

    def load(self,config,file,columns,average=True):
        """Load meta data from h5 file.

        Parameters
        ----------
        config: dict,
            h5 data configuration
        file: string
            file name
        columns: dict
            Specify column header and h5 data path to meta datam i.e.
                columns = dict()
                columns['Sample Stage horz'] = 'Endstation/Motors/ssh
                ...
        average: Boolean
            determines if array of values or their average is reported
        """

        self.df = get_spreadsheet(config,file,columns,average=average)

    def show(self):
        """Display the spreadsheet as pandas DataFrame"""

        return self.df
    
    def export(self,filename):
        """Export the created spreadsheet in csv format as log file.

        Parameters
        ----------
        filename: string
            file name of the created csv file
        """

        self.df.to_csv(f"{filename}.csv")
        return self.df

#########################################################################################
#########################################################################################

def getBL(config, file, stream, *args, average=False):
    """Load beamline meta data.

        Parameters
        ----------
        config: dict,
            h5 data configuration
        file: string
            file name
        keys: string, list
            path to the meta data of interest
        args: int
            scan numbers, comma separated
        kwargs:
            average: Boolean
                determines if array of values or their average is reported
    """
    
    get_single_beamline_value(config, file, stream, *args, average=average)

#########################################################################################
#########################################################################################
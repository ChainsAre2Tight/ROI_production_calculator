import tkinter as tk
import tkinter.messagebox

from backend.product import Product
from backend.get_products import get_products
from backend.functions import get_requirements_of_a_product, factories_from_demand
from tkinter import ttk
from dataclasses import dataclass
from frontend.text_converters import convert_factories_to_output_format, convert_requirements_to_output_format


class NotSelectedError(Exception):
    pass


class NoProductError(Exception):
    pass


@dataclass
class Widgets:
    main_frame: tk.Frame

    frame_top: tk.Frame
    frame_left: tk.Frame
    frame_right: tk.Frame

    frame_product: tk.Frame
    label_product: tk.Label
    product_combobox: ttk.Combobox

    frame_simplified: tk.Frame
    simplified_checkbutton: tk.Checkbutton

    frame_demand: tk.Frame
    label_demand: tk.Label
    demand_entry: tk.Entry

    frame_per: tk.Frame
    label_per: tk.Label
    per_entry: tk.Entry

    frame_output: tk.Frame
    output_label: tk.Label

    frame_bottom_buttons: tk.Frame
    button_calculate_requirements: tk.Button
    button_calculate_factories: tk.Button
    refresh_products_button: tk.Button


class Window:
    root: tk.Tk
    _products: dict
    _products_var: tk.StringVar
    widgets: Widgets
    _simplified_production_chains: tk.BooleanVar  # TODO implement
    _demand: tk.IntVar
    _per: tk.IntVar
    _output_text = tk.StringVar

    pad = 5
    geometry = '400x400'
    title = 'Calculator'

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.title)
        # self.root.geometry(self.geometry)
        self.root.resizable(False, False)
        self._products = get_products()
        self._products_var = tk.StringVar(value='Select a product')
        self._simplified_production_chains = tk.BooleanVar(value=True)
        self._demand = tk.IntVar(value=1)
        self._per = tk.IntVar(value=15)
        self._output_text = tk.StringVar(value='There will be displayed results of the calculations')

        self.initialize_ui()

    @property
    def list_of_products(self) -> list:
        return list(self._products.keys())

    def refresh_products(self):
        self._products = get_products()

    @property
    def products(self):
        return self._products

    @property
    def simplified_production_chains(self) -> bool:
        return self._simplified_production_chains.get()

    @property
    def products_var(self) -> str:
        return self._products_var.get()

    @property
    def current_product(self) -> Product:
        p_name = self.products_var
        if p_name == 'Select a product':
            raise NotSelectedError('No product is selected')
        try:
            return self.products[p_name]
        except KeyError:
            raise NoProductError(f'There is no such product "{p_name}" in products.py config')

    @property
    def demand(self) -> int:
        res = self._demand.get()
        if res <= 0:
            raise ValueError('Demand must be >= 0')
        return res

    @property
    def per(self) -> int:
        res = self._per.get()
        if res <= 0:
            raise ValueError('Period must be > 0')
        return res

    @property
    def output_text(self) -> str:
        return self._output_text.get()

    @output_text.setter
    def output_text(self, text):
        self._output_text.set(value=text)

    @staticmethod
    def show_warning_simplified():
        """Show a warning as disabled simplified production are not currently supported"""
        tkinter.messagebox.showwarning(title='Warning',
                                       message='Disabled simplified production chains are not currently supported')

    @staticmethod
    def show_no_product_error(msg):
        tkinter.messagebox.showerror(title='Warning',
                                     message=msg)

    @staticmethod
    def show_incorrect_input_error(msg):
        tkinter.messagebox.showerror(
            title='Error',
            message=f'Incorrect input: {msg}'
        )

    def calculate_requirements(self):
        if not self.simplified_production_chains:
            self.show_warning_simplified()
        try:
            cur_product = self.current_product
            amount = self.demand
            result = get_requirements_of_a_product(
                product=cur_product,
                amount=amount,
            )
            self.output_text = convert_requirements_to_output_format(result)
        except NoProductError as er:
            self.show_no_product_error(er.args[0])
        except ValueError as er:
            self.show_incorrect_input_error(er.args[0])
        except NotSelectedError:
            pass

    def calculate_factories(self):
        if not self._simplified_production_chains:
            self.show_warning_simplified()
        try:
            cur_product = self.current_product
            amount = self.demand
            period = self.per
            result = factories_from_demand(
                product=cur_product,
                required=amount,
                per=period,
            )
            self.output_text = convert_factories_to_output_format(result)
        except NoProductError as er:
            self.show_no_product_error(er.args[0])
        except ValueError as er:
            self.show_incorrect_input_error(er.args[0])
        except NotSelectedError:
            pass

    def initialize_ui(self):
        # main window frame
        frame_main = tk.Frame(self.root)
        frame_main.pack(side='top', fill='both')

        # frame for inputs
        frame_top = tk.Frame(master=frame_main)
        frame_top.pack(side='top', fill='x')

        # frame for leftmost widgets
        frame_left = tk.Frame(master=frame_top)
        frame_left.pack(side='left', fill='y')

        # frame for rightmost widgets
        frame_right = tk.Frame(master=frame_top)
        frame_right.pack(side='right', fill='y')

        # product selection
        frame_product = tk.Frame(master=frame_left)
        frame_product.pack(side='top', fill='x')

        label_product = tk.Label(master=frame_product, text='Select a product')
        label_product.pack(side='left', padx=self.pad, pady=self.pad)

        combobox = ttk.Combobox(
            master=frame_product,
            textvariable=self._products_var,
            values=self.list_of_products,
            width=20, )
        combobox.pack(side='left', padx=self.pad, pady=self.pad)

        # simplified production chains checkbox
        frame_simplified = tk.Frame(master=frame_left)
        frame_simplified.pack(side='top', fill='x')

        simplified_checkbutton = tk.Checkbutton(
            master=frame_simplified,
            variable=self._simplified_production_chains,
            text='Simplified production chains'
        )
        simplified_checkbutton.pack(side='left', padx=self.pad, pady=self.pad)

        # demand entry and Co.
        frame_demand = tk.Frame(master=frame_right)
        frame_demand.pack(side='top', fill='x')

        label_demand = tk.Label(master=frame_demand, text='Enter demand')
        label_demand.pack(side='left', padx=self.pad, pady=self.pad)

        demand_entry = tk.Entry(master=frame_demand, textvariable=self._demand)
        demand_entry.pack(side='right', padx=self.pad, pady=self.pad)

        # demand entry and Co.
        frame_per = tk.Frame(master=frame_right)
        frame_per.pack(side='top', fill='x')

        label_per = tk.Label(master=frame_per, text='Enter period in days')
        label_per.pack(side='left', padx=self.pad, pady=self.pad)

        per_entry = tk.Entry(master=frame_per, textvariable=self._per)
        per_entry.pack(side='right', padx=self.pad, pady=self.pad)

        # output box
        frame_output = tk.Frame(master=frame_main)
        frame_output.pack(side='top', padx=self.pad, pady=self.pad)

        output_label = tk.Label(master=frame_output, textvariable=self._output_text, width=40, justify='left')
        output_label.pack(side='top', padx=self.pad, pady=self.pad, fill='both')

        # frame for buttons at the bottom of the window
        frame_bottom = tk.Frame(master=frame_main)
        frame_bottom.pack(side='bottom', padx=self.pad, pady=self.pad)

        button_calculate_requirements = tk.Button(
            master=frame_bottom,
            command=self.calculate_requirements,
            text='Calculate requirements',
        )
        button_calculate_requirements.pack(side='left', padx=1)

        button_calculate_factories = tk.Button(
            master=frame_bottom,
            command=self.calculate_factories,
            text='Calculate factories',
        )
        button_calculate_factories.pack(side='left', padx=1)

        button_refresh_products = tk.Button(
            master=frame_bottom,
            command=self.refresh_products,
            text='Refresh products',
        )
        button_refresh_products.pack(side='left', padx=1)

        self.widgets = Widgets(
            main_frame=frame_main,
            frame_left=frame_left,
            frame_right=frame_right,
            frame_top=frame_top,
            product_combobox=combobox,
            label_product=label_product,
            frame_product=frame_product,
            frame_simplified=frame_simplified,
            simplified_checkbutton=simplified_checkbutton,
            frame_demand=frame_demand,
            label_demand=label_demand,
            demand_entry=demand_entry,
            frame_per=frame_per,
            label_per=label_per,
            per_entry=per_entry,
            frame_output=frame_output,
            output_label=output_label,
            frame_bottom_buttons=frame_bottom,
            button_calculate_requirements=button_calculate_requirements,
            button_calculate_factories=button_calculate_factories,
            refresh_products_button=button_refresh_products,
        )


if __name__ == "__main__":
    w = Window()
    w.root.mainloop()

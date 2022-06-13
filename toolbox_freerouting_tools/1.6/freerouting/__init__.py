#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 01/26/2021
"""Docstring for module __init__.py"""

# Imports - standard library
import os
from typing import Callable, List
import subprocess

# Imports - 3rd party packages
from toolbox.tool import Tool, ToolError
from toolbox.database import Database
from toolbox.logger import LogLevel
from toolbox.utils import *
from jinja2 import StrictUndefined, Environment, FileSystemLoader

# Imports - local source
from jinja_tool import JinjaTool


class FreeRoutingTool(JinjaTool):
    """Xilinx synthesis and implementation tool"""
    def __init__(self, db: Database, log: Callable[[str, LogLevel], None]):
        super(FreeRoutingTool, self).__init__(db, log)
        self.free = self.get_db(self.get_namespace("FreeRoutingTool"))
        self.bin = BinaryDriver("java")
        self.template_file = "my_rules.rules"
        self.render_file = os.path.join(self.get_db("internal.job_dir"), self.template_file)

    def steps(self) -> List[Callable[[], None]]:
        """Returns a list of functions to run for each step"""
        return [self.render_rules, self.run_freerouting]

    def render_rules(self):
        """Renders tcl file that vivado will run in batch mode"""
        self.render_to_file(self.template_file, self.render_file)

    def run_freerouting(self):
        """Actually runs the freerouting command"""
        if self.free["execute"]:
            # Add options
            self.bin.add_option("-jar", str(Path(self.free["jar"]).resolve()))
            self.bin.add_option("-de", str(Path(self.free["dsn_file"]).resolve()))
            if self.free['rules_file']:
                self.bin.add_option("-dr", str(Path(self.free['rules_file']).resolve()))
            else:
                self.bin.add_option("-dr", str(Path(self.render_file).resolve()))
            self.bin.add_option("-do", f"output.{self.free['output_format']}")
            self.bin.add_option("-mp", self.free["num_passes"])
            if self.free['excluded_net_classes']:
                self.bin.add_option('-inc', ','.join(self.free['excluded_net_classes']))
            if self.free['num_threads']:
                self.bin.add_option("-mt", self.free["num_threads"])
            if self.free["language"] != "english":
                self.bin.add_option("-l", "de")
            # Execute binary
            self.log(self.bin.get_execute_string())
            self.bin.execute(directory=self.get_db('internal.job_dir'))
            self.log(
                f"Final implementation in => {Path(self.get_db('internal.job_dir')).relative_to(self.get_db('internal.work_dir'))}"
            )
        else:
            self.log(
                "Freerouting implement execute flag set to false. Design not routed."
            )

import type { MystPlugin } from 'myst-common';
import { npdocJsonDirective } from './npdocJsonDirective.js';
import { versionAddedDirective } from './versionAdded.js';
import { funcRole } from './funcRole.js';

const plugin: MystPlugin = {
  name: 'Plugin to document Python API using npdoc2json output',
  author: 'Franklin Koch',
  license: 'MIT',
  transforms: [],
  directives: [npdocJsonDirective, versionAddedDirective],
  roles: [funcRole],
};

export default plugin;

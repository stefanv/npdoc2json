# npdoc-json-plugin

MyST plugin for rendering API docs from npdoc2json output

![](./thumbnail.png)

## Development

To develop this package, you may run

```bash
npm install
npm run lint
```

Then, to add the plugin to your MyST build, you must build the `.mjs` file:

```bash
npm run build
```

Then link to the built file from you `myst.yml`:

```yaml
project:
  ...
  plugins:
    - npdoc-json-plugin/dist/index.mjs
```

## Plugin Usage

In your markdown you may now reference a `npdoc2json` output to render the full documentation:

```md
:::{npdoc} ./skimage.json
:::
```

You can specify the module name and heading depth as options:

```md
:::{npdoc} ./skimage.json
:module: skimage
:depth: 2
:::
```

You can also target a specific submodule:

```md
:::{npdoc} ./skimage.json#color
:module: skimage
:depth: 2
:::
```

or a specific function:

```md
:::{npdoc} ./skimage.json#color.lch2lab
:module: skimage
:depth: 2
:::
```
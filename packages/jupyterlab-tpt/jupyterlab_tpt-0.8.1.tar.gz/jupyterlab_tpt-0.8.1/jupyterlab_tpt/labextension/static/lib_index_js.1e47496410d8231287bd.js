"use strict";
(self["webpackChunkjupyterlab_tpt"] = self["webpackChunkjupyterlab_tpt"] || []).push([["lib_index_js"],{

/***/ "./lib/admonitions.js":
/*!****************************!*\
  !*** ./lib/admonitions.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   insert_solution: () => (/* binding */ insert_solution),
/* harmony export */   toggle_admonition: () => (/* binding */ toggle_admonition)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* eslint-disable prettier/prettier */

const FENCE = '````';
/* works on the active cell */
const toggle_admonition = (notebook, admonition) => {
    const activeCell = notebook === null || notebook === void 0 ? void 0 : notebook.activeCell;
    if (activeCell === undefined) {
        return;
    }
    const model = activeCell === null || activeCell === void 0 ? void 0 : activeCell.model;
    if (model === undefined) {
        return;
    }
    _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookActions.changeCellType(notebook, 'markdown');
    let cell_source = model.sharedModel.getSource();
    // remove trailing newlines
    while (cell_source.endsWith('\n')) {
        cell_source = cell_source.slice(0, -1);
    }
    // does it start with an admonition?
    const turning_off = cell_source.startsWith(FENCE);
    console.debug('admonition: turning_off', turning_off);
    // a function that removes any initial white line, and any trailing white line
    // a line is considered white if it is empty or only contains whitespace
    const tidy = (dirty) => {
        const lines = dirty.split('\n');
        while (lines.length !== 0 && lines[0].match(/^\s*$/)) {
            lines.shift();
        }
        while (lines.length !== 0 && lines[lines.length - 1].match(/^\s*$/)) {
            lines.pop();
        }
        return lines.join('\n');
    };
    let new_source;
    if (turning_off) {
        new_source = tidy(cell_source
            .replace(RegExp(`^${FENCE} *{[a-zA-Z]+}`), '')
            .replace(RegExp(`\n${FENCE}$`), ''));
    }
    else {
        new_source = `${FENCE}{${admonition}}\n${tidy(cell_source)}\n${FENCE}`;
    }
    model.sharedModel.setSource(new_source);
};
// works on the active cell and simply insert a solution block
// at cursor location
const insert_solution = (notebook, visible, filename) => {
    const activeCell = notebook === null || notebook === void 0 ? void 0 : notebook.activeCell;
    if ((!activeCell) || (!activeCell.editor))
        return;
    const model = activeCell === null || activeCell === void 0 ? void 0 : activeCell.model;
    if (model === undefined) {
        return;
    }
    // const cell_source = model.sharedModel.getSource()
    const cursor = activeCell.editor.getCursorPosition();
    // const line = cursor.line
    // const ch = cursor.ch
    console.log('cursor', cursor);
    // const new_source = `${cell_source.slice(0, ch)}\n\n\`\`\`{solution} ${visible} ${filename}\n\n${cell_source.slice(ch)}`
    // model.sharedModel.setSource(new_source)
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! jupyterlab-celltagsclasses */ "./node_modules/jupyterlab-celltagsclasses/lib/metadata.js");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! jupyterlab-celltagsclasses */ "./node_modules/jupyterlab-celltagsclasses/lib/apply_on_cells.js");
/* harmony import */ var _style_selected_cells_raw_css__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../style/selected_cells.raw.css */ "./style/selected_cells.raw.css");
/* harmony import */ var _admonitions__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./admonitions */ "./lib/admonitions.js");
/*
 * for attaching keybindings later on, see
 * https://towardsdatascience.com/how-to-customize-jupyterlab-keyboard-shortcuts-72321f73753d
 */



// md_clean may be broken





const PLUGIN_ID = 'jupyterlab-tpt:plugin';
// metadata
// md_clean may be broken
// import { md_set, , md_insert, md_remove } from 'jupyterlab-celltagsclasses'
const clean_cell_metadata = (cell) => {
    console.log('Cleaning metadata for cell', cell);
    const editable = cell.model.getMetadata('editable');
    if (editable === true) {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_unset)(cell, 'editable');
    }
    const tags = cell.model.getMetadata('tags');
    if ((tags === null || tags === void 0 ? void 0 : tags.length) === 0) {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_unset)(cell, 'tags');
    }
    const slide_type = (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_get)(cell, 'slideshow.slide_type');
    if (slide_type === '') {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_unset)(cell, 'slideshow.slide_type');
    }
    const slideshow = (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_get)(cell, 'slideshow');
    if (slideshow !== undefined && JSON.stringify(slideshow) === '{}') {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_unset)(cell, 'slideshow');
    }
    const user_expressions = (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_get)(cell, 'user_expressions');
    if ((user_expressions === null || user_expressions === void 0 ? void 0 : user_expressions.length) === 0) {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_unset)(cell, 'user_expressions');
    }
};
// cells that have this in their code
const NEEDLE = 'tools.sample_from';
const set_remove_input_needle = (cell, hidden) => {
    // ignore text cells
    if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCell) {
        // need to access the cell model
        const model = cell.model;
        if (model.sharedModel.getSource().toLowerCase().indexOf(NEEDLE) !== -1) {
            if (hidden) {
                (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_remove)(cell, 'tags', 'remove-input');
            }
            else {
                (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_insert)(cell, 'tags', 'remove-input');
            }
        }
    }
};
// use depth=0 to remove
const make_text_and_insert_section = (notebook, depth) => {
    // console.log("make_text_and_insert_section", depth)
    _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookActions.changeCellType(notebook, 'markdown');
    const activeCell = notebook === null || notebook === void 0 ? void 0 : notebook.activeCell;
    if (activeCell === undefined) {
        return;
    }
    const model = activeCell === null || activeCell === void 0 ? void 0 : activeCell.model;
    if (model === undefined) {
        return;
    }
    // remove starting #'s if any
    for (let i = 4; i > 0; i--) {
        model.sharedModel.setSource(model.sharedModel.getSource().replace('#'.repeat(i) + ' ', ''));
    }
    if (depth === 0) {
        return;
    }
    model.sharedModel.setSource(`${'#'.repeat(depth)} ${model.sharedModel.getSource()}`);
};
const toggle_tag = (cell, tag) => {
    if ((0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_get)(cell, 'tags', tag)) {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_remove)(cell, 'tags', tag);
    }
    else {
        (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_insert)(cell, 'tags', tag);
    }
};
/**
 * Initialization data for the jupyterlab-tpt extension.
 */
const plugin = {
    id: 'jupyterlab-tpt:plugin',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry],
    activate: (app, palette, notebookTracker, settingRegistry) => {
        console.log('JupyterLab extension jupyterlab-tpt is activating');
        // console.log('ICommandPalette', palette)
        // console.log('INotebookTracker', notebookTracker)
        // the addCommand would accept the following
        // isEnabled: () => true,
        // isVisible: () => true,
        // iconClass: 'some-css-icon-class',
        // also we could pass args to execute, but in the hide-input case
        // it does not work well as we need distinct labels depending on the args
        // https://lumino.readthedocs.io/en/1.x/api/commands/interfaces/commandregistry.ikeybindingoptions.html
        // The supported modifiers are: Accel, Alt, Cmd, Ctrl, and Shift. The Accel
        // modifier is translated to Cmd on Mac and Ctrl on all other platforms. The
        // Cmd modifier is ignored on non-Mac platforms.
        // Alt is option on mac
        let [outline_selected_cells] = [false];
        let command;
        command = 'metadata:clean-selected';
        app.commands.addCommand(command, {
            label: 'clean metadata for all selected cells',
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.Multiple, clean_cell_metadata)
        });
        palette.addItem({ command, category: 'metadata' });
        app.commands.addKeyBinding({
            command,
            keys: ['Alt Cmd 7'],
            selector: '.jp-Notebook'
        });
        command = 'metadata:clean-all';
        app.commands.addCommand(command, {
            label: 'clean metadata for all cells',
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.All, clean_cell_metadata)
        });
        palette.addItem({ command, category: 'metadata' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl Alt 7'],
            selector: '.jp-Notebook'
        });
        // Option-Command-9 = toggle (hide-input) on all selected cells
        // Ctrl-Alt-9 = show (wrt hide-input) on all selected cells
        command = 'convenience:show-settings';
        app.commands.addCommand(command, {
            label: 'show settings',
            execute: () => console.log(`Current settings: outline_selected_cells = ${outline_selected_cells}`)
        });
        palette.addItem({ command, category: 'Convenience' });
        // app.commands.addKeyBinding({ command, keys: ['Alt Cmd 7'], selector: '.jp-Notebook' })
        command = 'convenience:hide-input-all-samples';
        app.commands.addCommand(command, {
            label: `remove input for all code cells that contain ${NEEDLE}`,
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.All, cell => set_remove_input_needle(cell, true))
        });
        palette.addItem({ command, category: 'convenience' });
        app.commands.addKeyBinding({
            command,
            keys: ['Alt Cmd 8'],
            selector: '.jp-Notebook'
        });
        command = 'convenience:show-input-all-samples';
        app.commands.addCommand(command, {
            label: `reinstate input for all code cells that contain ${NEEDLE}`,
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.All, cell => set_remove_input_needle(cell, false))
        });
        palette.addItem({ command, category: 'convenience' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl Alt 8'],
            selector: '.jp-Notebook'
        });
        // Ctrl-0 to Ctrl-4 to set markdown sections
        for (let depth = 0; depth < 5; depth++) {
            command = `convenience:section-level-${depth}`;
            app.commands.addCommand(command, {
                label: `active cell becomes section level ${depth}`,
                execute: () => {
                    var _a;
                    const notebook = (_a = notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                    if (notebook === undefined) {
                        return;
                    }
                    make_text_and_insert_section(notebook, depth);
                }
            });
            palette.addItem({ command, category: 'convenience' });
            app.commands.addKeyBinding({
                command,
                keys: [`Ctrl ${depth}`],
                selector: '.jp-Notebook'
            });
        }
        // render-all-cells - unrender-all-cells (markdown actually)
        const unrender_markdown = (cell) => {
            if (cell.model.type !== 'markdown') {
                return;
            }
            cell.rendered = false;
        };
        command = 'notebook:unrender-all-markdown';
        app.commands.addCommand(command, {
            label: 'unrender all markdown cells',
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.All, unrender_markdown)
        });
        palette.addItem({ command, category: 'convenience' });
        // control-e means end of ine if in edit mode
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl E'],
            selector: '.jp-Notebook.jp-mod-commandMode'
        });
        app.commands.addKeyBinding({
            command: 'notebook:render-all-markdown',
            keys: ['Ctrl W'],
            selector: '.jp-Notebook'
        });
        // this is actually lowercase u and d, would need an explicit Shift otherwise
        app.commands.addKeyBinding({
            command: 'notebook:move-cell-up',
            keys: ['U'],
            selector: '.jp-Notebook.jp-mod-commandMode'
        });
        app.commands.addKeyBinding({
            command: 'notebook:move-cell-down',
            keys: ['D'],
            selector: '.jp-Notebook.jp-mod-commandMode'
        });
        command = 'convenience:toggle-raises-exception';
        app.commands.addCommand(command, {
            label: 'toggle raises-exception for all selected cells',
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.Multiple, cell => toggle_tag(cell, 'raises-exception'))
        });
        palette.addItem({ command, category: 'convenience' });
        app.commands.addKeyBinding({
            command,
            keys: ['Alt Cmd 6'],
            selector: '.jp-Notebook'
        });
        command = 'convenience:set-raises-exception';
        app.commands.addCommand(command, {
            label: 'set raises-exception for all selected cells',
            execute: () => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_6__.Scope.Multiple, cell => (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_5__.md_insert)(cell, 'tags', 'raises-exception'))
        });
        palette.addItem({ command, category: 'convenience' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl Alt 6'],
            selector: '.jp-Notebook'
        });
        const apply_outline_selected_cells = (outline_selected_cells) => {
            const id = 'outline-selected-cells-style';
            const present = document.getElementById(id);
            // already good
            if ((outline_selected_cells && present) ||
                (!outline_selected_cells && !present)) {
                return;
            }
            // need to inject
            if (outline_selected_cells) {
                console.log('injecting css for outlining selection');
                const inject_css = (css_text, id) => {
                    const style = document.createElement('style');
                    style.setAttribute('type', 'text/css');
                    style.id = id;
                    style.appendChild(document.createTextNode(css_text));
                    document.body.appendChild(style);
                };
                inject_css(_style_selected_cells_raw_css__WEBPACK_IMPORTED_MODULE_4__, id);
            }
            else {
                console.log('removing css for outlining selection');
                present === null || present === void 0 ? void 0 : present.remove();
            }
        };
        // admonitions
        for (const [name, key] of [
            ['admonition', 'Ctrl A'],
            ['tip', 'Ctrl T'],
            ['note', 'Ctrl N'],
            ['attention', null],
            ['caution', null],
            ['danger', null],
            ['error', null],
            ['hint', null],
            ['important', null],
            ['seealso', null],
            ['warning', null]
        ]) {
            // need to cast because name is typed as string | null ?!?
            const admonition = name;
            command = 'admonition:toggle';
            let label = 'toggle admonition';
            if (admonition !== 'admonition') {
                command += `-${admonition}`;
                label += ` ${admonition}`;
            }
            app.commands.addCommand(command, {
                label,
                execute: () => {
                    var _a;
                    const notebook = (_a = notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                    if (notebook === undefined) {
                        return;
                    }
                    (0,_admonitions__WEBPACK_IMPORTED_MODULE_7__.toggle_admonition)(notebook, admonition);
                }
            });
            palette.addItem({ command, category: 'admonition' });
            if (key !== null) {
                app.commands.addKeyBinding({
                    command,
                    keys: ['Ctrl \\', key],
                    selector: '.jp-Notebook'
                });
            }
        }
        // solution
        command = 'admonition:insert-solution';
        app.commands.addCommand(command, {
            label: 'insert a solution block at cursor location',
            execute: () => {
                var _a;
                const notebook = (_a = notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (notebook === undefined) {
                    return;
                }
                (0,_admonitions__WEBPACK_IMPORTED_MODULE_7__.insert_solution)(notebook, 'ouvrez-moi', 'xxx.py');
            }
        });
        palette.addItem({ command, category: 'convenience' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl \\', 'Ctrl S'],
            selector: '.jp-Notebook'
        });
        function loadSetting(setting) {
            // Read the settings and convert to the correct type
            outline_selected_cells = setting.get('outline_selected_cells')
                .composite;
            console.log(`tpt extension, outline_selected is read as ${outline_selected_cells}`);
            apply_outline_selected_cells(outline_selected_cells);
        }
        Promise.all([app.restored, settingRegistry.load(PLUGIN_ID)]).then(([_, setting]) => {
            loadSetting(setting);
            setting.changed.connect(loadSetting);
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./style/selected_cells.raw.css":
/*!**************************************!*\
  !*** ./style/selected_cells.raw.css ***!
  \**************************************/
/***/ ((module) => {

module.exports = "/* stylelint-disable */\n\n/* multiple selection - might be better suited in courselevels ? */\n.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {\n  background-image: url('data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"4\" height=\"4\" viewBox=\"0 0 4 4\"><path fill-opacity=\"0.4\" d=\"M1 3h1v1H1V3zm2-2h1v1H3V1z\"></path></svg>') !important;\n}\n\n/* stylelint-enable */\n";

/***/ })

}]);
//# sourceMappingURL=lib_index_js.1e47496410d8231287bd.js.map
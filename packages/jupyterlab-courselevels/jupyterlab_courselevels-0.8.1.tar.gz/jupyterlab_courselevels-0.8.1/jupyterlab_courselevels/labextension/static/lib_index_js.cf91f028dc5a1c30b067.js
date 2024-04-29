"use strict";
(self["webpackChunkjupyterlab_courselevels"] = self["webpackChunkjupyterlab_courselevels"] || []).push([["lib_index_js"],{

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
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! jupyterlab-celltagsclasses */ "webpack/sharing/consume/default/jupyterlab-celltagsclasses/jupyterlab-celltagsclasses");
/* harmony import */ var jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__);
/*
 * for attaching keybindings later on, see
 * https://towardsdatascience.com/how-to-customize-jupyterlab-keyboard-shortcuts-72321f73753d
 */







const PLUGIN_ID = 'jupyterlab-courselevels:plugin';
const ALL_LEVELS = ['basic', 'intermediate', 'advanced'];
const plugin = {
    id: PLUGIN_ID,
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry],
    activate: (app, palette, notebookTracker, settingRegistry) => {
        console.log('extension jupyterlab-courselevels is activating');
        // https://lumino.readthedocs.io/en/1.x/api/commands/interfaces/commandregistry.ikeybindingoptions.html
        // The supported modifiers are: Accel, Alt, Cmd, Ctrl, and Shift. The Accel
        // modifier is translated to Cmd on Mac and Ctrl on all other platforms. The
        // Cmd modifier is ignored on non-Mac platforms.
        // Alt is option on mac
        let [show_level_buttons] = [false];
        const ALL_FULL_LEVELS = ALL_LEVELS.map(level => `level_${level}`);
        const cell_toggle_level = (cell, level) => {
            const full_level = `level_${level}`;
            return (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.md_toggle_multi)(cell, 'tags', full_level, ALL_FULL_LEVELS);
        };
        const toggle_level = (level) => {
            (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.Scope.Multiple, (cell) => {
                cell_toggle_level(cell, level);
            });
        };
        let command;
        for (const [level, key] of [
            ['basic', 'Ctrl X'],
            ['intermediate', 'Ctrl Y'],
            ['advanced', 'Ctrl Z']
        ]) {
            command = `courselevels:toggle-level-${level}`;
            app.commands.addCommand(command, {
                label: `toggle ${level} level`,
                execute: () => toggle_level(level)
            });
            palette.addItem({ command, category: 'courselevels' });
            app.commands.addKeyBinding({
                command,
                keys: ['Ctrl \\', key],
                selector: '.jp-Notebook'
            });
        }
        const toggle_frame = () => {
            (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.Scope.Multiple, (cell) => {
                (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.md_toggle)(cell, 'tags', 'framed_cell');
            });
        };
        command = 'courselevels:toggle-frame';
        app.commands.addCommand(command, {
            label: 'toggle frame',
            execute: () => toggle_frame()
        });
        palette.addItem({ command, category: 'courselevels' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl \\', 'Ctrl M'],
            selector: '.jp-Notebook'
        });
        const toggle_licence = () => {
            (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.apply_on_cells)(notebookTracker, jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.Scope.Active, (cell) => {
                (0,jupyterlab_celltagsclasses__WEBPACK_IMPORTED_MODULE_4__.md_toggle)(cell, 'tags', 'licence');
            });
        };
        command = 'courselevels:toggle-licence';
        app.commands.addCommand(command, {
            label: 'toggle licence',
            execute: () => toggle_licence()
        });
        palette.addItem({ command, category: 'courselevels' });
        app.commands.addKeyBinding({
            command,
            keys: ['Ctrl \\', 'Ctrl L'],
            selector: '.jp-Notebook'
        });
        // the buttons in the toolbar
        const create_level_buttons = () => {
            const find_spacer = (panel) => {
                let index = 0;
                for (const child of panel.toolbar.children()) {
                    if (child.node.classList.contains('jp-Toolbar-spacer')) {
                        return index;
                    }
                    else {
                        index += 1;
                    }
                }
                return 0;
            };
            class BasicButton {
                createNew(panel, context) {
                    const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
                        className: 'courselevels-button',
                        iconClass: 'far fa-hand-pointer',
                        onClick: () => toggle_level('basic'),
                        tooltip: 'Toggle basic level'
                    });
                    // compute where to insert it
                    const index = find_spacer(panel);
                    panel.toolbar.insertItem(index, 'basicLevel', button);
                    return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__.DisposableDelegate(() => {
                        button.dispose();
                    });
                }
            }
            app.docRegistry.addWidgetExtension('Notebook', new BasicButton());
            class IntermediateButton {
                createNew(panel, context) {
                    const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
                        className: 'courselevels-button',
                        iconClass: 'far fa-hand-peace',
                        onClick: () => toggle_level('intermediate'),
                        tooltip: 'Toggle intermediate level'
                    });
                    // compute where to insert it
                    const index = find_spacer(panel);
                    panel.toolbar.insertItem(index, 'intermediateLevel', button);
                    return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__.DisposableDelegate(() => {
                        button.dispose();
                    });
                }
            }
            app.docRegistry.addWidgetExtension('Notebook', new IntermediateButton());
            class AdvancedButton {
                createNew(panel, context) {
                    const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
                        className: 'courselevels-button',
                        iconClass: 'far fa-hand-spock',
                        onClick: () => toggle_level('advanced'),
                        tooltip: 'Toggle advanced level'
                    });
                    // compute where to insert it
                    const index = find_spacer(panel);
                    panel.toolbar.insertItem(index, 'advancedLevel', button);
                    return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__.DisposableDelegate(() => {
                        button.dispose();
                    });
                }
            }
            app.docRegistry.addWidgetExtension('Notebook', new AdvancedButton());
            class FrameButton {
                createNew(panel, context) {
                    const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
                        className: 'courselevels-button',
                        iconClass: 'fas fa-crop-alt',
                        onClick: () => toggle_frame(),
                        tooltip: 'Toggle frame around cell'
                    });
                    // compute where to insert it
                    const index = find_spacer(panel);
                    panel.toolbar.insertItem(index, 'frameLevel', button);
                    return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__.DisposableDelegate(() => {
                        button.dispose();
                    });
                }
            }
            app.docRegistry.addWidgetExtension('Notebook', new FrameButton());
        };
        // load settings and create buttons if requested
        function loadSetting(setting) {
            // Read the settings and convert to the correct type
            show_level_buttons = setting.get('show_level_buttons')
                .composite;
            console.log(`jupyterlab-courselevels extension: show_level_buttons is set to ${show_level_buttons}`);
            if (show_level_buttons) {
                create_level_buttons();
            }
        }
        // but do it only after the app has started
        Promise.all([app.restored, settingRegistry.load(PLUGIN_ID)]).then(([_, setting]) => {
            loadSetting(setting);
            setting.changed.connect(loadSetting);
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.cf91f028dc5a1c30b067.js.map
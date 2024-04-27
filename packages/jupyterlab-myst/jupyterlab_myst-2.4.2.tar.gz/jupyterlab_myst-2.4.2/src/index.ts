import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { IMarkdownViewerTracker } from '@jupyterlab/markdownviewer';

import { IEditorServices } from '@jupyterlab/codeeditor';

import {
  INotebookTracker,
  Notebook,
  NotebookActions,
  NotebookPanel
} from '@jupyterlab/notebook';
import { Cell } from '@jupyterlab/cells';
import { MySTContentFactory } from './MySTContentFactory';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { notebookCellExecuted } from './actions';
import { mystMarkdownRendererFactory } from './mime';

/**
 * The notebook content factory provider.
 */
const plugin: JupyterFrontEndPlugin<NotebookPanel.IContentFactory> = {
  id: 'jupyterlab-myst:content-factory',
  provides: NotebookPanel.IContentFactory,
  requires: [IEditorServices],
  autoStart: true,
  activate: (app: JupyterFrontEnd, editorServices: IEditorServices) => {
    console.log('JupyterLab extension jupyterlab-myst is activated!');
    const editorFactory = editorServices.factoryService.newInlineEditor;
    return new MySTContentFactory({ editorFactory });
  }
};

/**
 * The notebook cell executor.
 */
const executorPlugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-myst:executor',
  requires: [INotebookTracker],
  autoStart: true,
  activate: (app: JupyterFrontEnd, tracker: INotebookTracker) => {
    console.log('Using jupyterlab-myst:executor');

    NotebookActions.executed.connect(
      async (sender: any, value: { notebook: Notebook; cell: Cell }) => {
        const { notebook, cell } = value;
        await notebookCellExecuted(notebook, cell, tracker);
      }
    );

    return;
  }
};

const mimeRendererPlugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-myst:mime-renderer',
  requires: [IRenderMimeRegistry],
  autoStart: true,
  optional: [IMarkdownViewerTracker, ISettingRegistry],
  activate: (
    app: JupyterFrontEnd,
    registry: IRenderMimeRegistry,
    // We don't need this tracker directly, but it ensures that the built-in
    // Markdown renderer is registered, so that we can then safely add our own.
    tracker?: IMarkdownViewerTracker,
    settingRegistry?: ISettingRegistry
  ) => {
    console.log('Using jupyterlab-myst:mime-renderer');

    // Enable frontmatter by default
    if (settingRegistry) {
      settingRegistry
        .load('@jupyterlab/markdownviewer-extension:plugin')
        .then((settings: ISettingRegistry.ISettings) => {
          settings.set('hideFrontMatter', false);
        });
    }

    // Add the MyST markdown renderer factory.
    registry.addFactory(mystMarkdownRendererFactory);
  }
};

export default [plugin, executorPlugin, mimeRendererPlugin];

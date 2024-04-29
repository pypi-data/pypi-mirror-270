import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
  ILabShell,
} from '@jupyterlab/application';
import { ICommandPalette } from '@jupyterlab/apputils';
import '../style/index.css'; // 引入自定义CSS文件
import { IMainMenu } from '@jupyterlab/mainmenu';
import {IFileBrowserFactory} from '@jupyterlab/filebrowser';
import {INotebookTracker } from '@jupyterlab/notebook';
import { checkLogin } from './api';
const { MainAreaWidget } = require('@jupyterlab/apputils');
const { Widget } = require('@lumino/widgets');

/**
 * The command IDs used by the application plugin.
 */
// namespace CommandIDs {
//   export const createConsole = 'notebook:create-console';
// }

/**
 * Initialization data for the didi-notebook-extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'didi-notebook-extension:plugin',
  description: 'A JupyterLab extension.',
  autoStart: true,
  requires: [IMainMenu, IFileBrowserFactory, ICommandPalette, INotebookTracker],
  optional: [ILabShell],
  activate: async (
    app: JupyterFrontEnd,
    mainMenu: IMainMenu,
    factory: IFileBrowserFactory,
    palette: ICommandPalette, 
    tracker: INotebookTracker,
    labShell: ILabShell,
    ) => {
    // const trans = translator.load('jupyterlab');
    const urlParams = new URLSearchParams(window.location.search);
    const urlQueryFrom = urlParams.get('from');
    const hideMenu: string | false = urlParams.get('hideMenu') || false;
    console.log('-----didi-notebook-extension url query----', urlParams);
    // 创建一个新的Widget
    const content = new Widget();
    content.id = 'didi-notebook-extension-plugin-window';
    content.title.label = 'didi-notebook-extension Window';
    content.title.closable = true;
    // 内嵌在studio中
    if (urlQueryFrom === 'studio') {
      console.log('-----didi-notebook-extension----check from studio------');
      document.body.classList.add('from-studio');
      const isLogin = await checkLogin();
      if (!isLogin) {
        console.log('-----didi-notebook-extension----check login failed------');
        return ;
      }    
      console.log('-----didi-notebook-extension----check login success------')
    
      console.log('------from studio  window------', window);

      content.node.addEventListener('message', (res: any) => {
        console.log('---------didi-notebook-extension 收到数据啦啦啦啦啦啦---------', res.data);
        const data = res.data || {};
        if (data.event === 'studio-debug-mode-save') {
          app.commands.execute('docmanager:save');
        }
      });
      const widget = new MainAreaWidget({ content });
      labShell && labShell?.add(widget, 'main');

    }
    // 隐藏菜单
    if ( hideMenu === 'true' || hideMenu !== false) {

      // 隐藏菜单
      document.body.classList.add('hide-menu');
      if (labShell) { 
        // const contextNode: HTMLElement | undefined = app.contextMenuHitTest(
        //   node => !!node.dataset.id
        // );
        if (labShell.leftCollapsed) {
          labShell.expandLeft();
        }
        if (labShell.rightCollapsed) {
          labShell.expandRight();
        }
        labShell.activeChanged.connect((sender, args) => {
          if (sender.leftCollapsed) {
            sender.expandLeft();
          }
          if (sender.rightCollapsed) {
            sender.expandRight();
          }
        });
      }
    }
     // 监听文件保存事件
    factory.createFileBrowser('cur-file').model.fileChanged.connect((sender, args) => {
      if (args.type === 'save') {
        console.log('---didi-notebook-extension-----File saved-------');
        window.parent.postMessage({
          event: 'studio-debug-mode-save',
          key: 'save'
        }, '*');
      }
    });
    console.log('JupyterLab extension didinotebooktest is activated! log', urlQueryFrom, hideMenu);
    console.log('JupyterLab extension didi-notebook-extension is activated!', window, app);
  
  }
};

export default plugin;

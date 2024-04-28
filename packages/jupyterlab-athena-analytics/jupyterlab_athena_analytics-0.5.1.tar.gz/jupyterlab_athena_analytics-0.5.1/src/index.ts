import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { INotebookTracker, NotebookPanel, Notebook } from '@jupyterlab/notebook';
import { ICellModel } from '@jupyterlab/cells';

// Function to handle the event when the notebook content changes
function onNotebookChange(notebook: Notebook): void {
  if (!notebook.model) {
    console.error('Notebook model is null');
    return;
  }
  const notebookJSON = notebook.model.toJSON();
  window.parent.postMessage({
    type: 'notebookChange',
    data: notebookJSON
  }, '*');
}

function onTabChange(notebookPanel: NotebookPanel): void {
  if (!notebookPanel.content.model) {
    console.error('Notebook model is null');
    return;
  }
  const notebookJSON = notebookPanel.content.model.toJSON();
  window.parent.postMessage({
    type: 'tabChange',
    data: notebookJSON
  }, '*');
}

// Function to handle the event when the active cell changes
function onActiveCellChange(notebook: Notebook): void {
  const activeCell = notebook.activeCell;
  const cellData = activeCell?.model.toJSON();
  window.parent.postMessage({
    type: 'activeCellChange',
    data: cellData
  }, '*');
}

// Function to handle changes in any cell's content
function onCellModelChange(cellModel: ICellModel): void {
  const cellData = cellModel.toJSON();
  window.parent.postMessage({
    type: 'cellContentChange',
    data: cellData
  }, '*');
}

// Function to add listeners to each cell in the notebook
function addCellListeners(notebook: Notebook): void {
  notebook.widgets.forEach(cell => {
    cell.model.contentChanged.connect(() => onCellModelChange(cell.model));
  });
}

// Function to add the event listeners to a notebook panel
function addChangeListener(notebookPanel: NotebookPanel) {
  // Listen for content changes in the notebook
  notebookPanel.content.modelContentChanged.connect(() => onNotebookChange(notebookPanel.content));
  notebookPanel.content.activeCellChanged.connect(() => onActiveCellChange(notebookPanel.content));

  // Add listeners to each cell for content changes
  addCellListeners(notebookPanel.content);

  if (!notebookPanel?.content?.model) return;
  // Listen for when new cells are added to the notebook
  notebookPanel.content.model.cells.changed.connect(() => {
    addCellListeners(notebookPanel.content);
  });
}

/**
 * Initialization data for the jupyterlab_athena_analytics extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_athena_analytics:plugin',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, tracker: INotebookTracker) => {
    console.log(
      'JupyterLab extension jupyterlab_athena_analytics is activated!'
    );

    // Add change listener to all currently opened notebooks
    tracker.forEach((notebookPanel) => {
      addChangeListener(notebookPanel);
    });

    // Ensure that change listeners are added to new notebooks as they are opened
    tracker.widgetAdded.connect((sender, notebookPanel) => {
      addChangeListener(notebookPanel);
    });

    tracker.currentChanged.connect((sender, notebookPanel) => {
      if (notebookPanel) {
        onTabChange(notebookPanel);
      }
    });

    // Dynamically inject the PostHog analytics script into the document
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.async = true;
    script.innerHTML = `!function(t,e){var o,n,p,r;e._SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e._SV=1)}(document,window.posthog||[]);
    posthog.init('phc_klucwJxuBrgYuAXGSCOUGnp0qhKeA81OuIFyUngiPGQ',{api_host:'https://app.athenaintelligence.ai/ingest', ui_host: 'https://us.posthog.com', session_recording: { recordCrossOriginIframes: true }})`;
    document.head.appendChild(script);
  }
};

export default plugin;

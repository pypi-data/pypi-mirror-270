/* eslint-disable prettier/prettier */

import { Notebook, NotebookActions } from '@jupyterlab/notebook'

const FENCE3 = '```'
const FENCE4 = '````'

/* works on the active cell */
export const toggle_admonition = (
  notebook: Notebook,
  admonition: string
): void => {
  const activeCell = notebook?.activeCell
  if (activeCell === undefined) {
    return
  }
  const model = activeCell?.model
  if (model === undefined) {
    return
  }

  NotebookActions.changeCellType(notebook, 'markdown')

  let cell_source = model.sharedModel.getSource()
  // remove trailing newlines
  while (cell_source.endsWith('\n')) {
    cell_source = cell_source.slice(0, -1)
  }
  // does it start with an admonition?
  const turning_off = cell_source.startsWith(FENCE4)

  console.debug('admonition: turning_off', turning_off)

  // a function that removes any initial white line, and any trailing white line
  // a line is considered white if it is empty or only contains whitespace
  const tidy = (dirty: string): string => {
    const lines = dirty.split('\n')
    while (lines.length !== 0 && lines[0].match(/^\s*$/)) {
      lines.shift()
    }
    while (lines.length !== 0 && lines[lines.length - 1].match(/^\s*$/)) {
      lines.pop()
    }
    return lines.join('\n')
  }

  let new_source: string
  if (turning_off) {
    new_source = tidy(
      cell_source
        .replace(RegExp(`^${FENCE4} *{[a-zA-Z]+}`), '')
        .replace(RegExp(`\n${FENCE4}$`), '')
    )
  } else {
    new_source = `${FENCE4}{${admonition}}\n${tidy(cell_source)}\n${FENCE4}`
  }

  model.sharedModel.setSource(new_source)
}

// works on the active cell and simply insert a solution block
// at cursor location

const index_from_line_column = (input: string, line: number, column: number) => {
  let lineno = 0
  let colno = 0
  let counter = 0
  for (const ch of input) {
    if (lineno === line && colno === column) {
      return counter
    }
    if (ch === '\n') {
      lineno += 1
      colno = 0
    } else {
      colno += 1
    }
    counter += 1
  }
}

export const insert_solution = (
  notebook: Notebook,
  visible: string,
  filename: string,
): void => {
  const activeCell = notebook?.activeCell
  if ((!activeCell) || (!activeCell.editor)) return

  const model = activeCell?.model
  if (model === undefined) {
    return
  }

  const before = model.sharedModel.getSource()
  console.log('cell_source', typeof before, before)
  const {line, column} = activeCell.editor.getCursorPosition()
  const cursor = index_from_line_column(before, line, column)
  const begin = before.slice(0, cursor)
  const end = before.slice(cursor)

  let to_insert = `### solution\n\n${FENCE4}{admonition} ${visible}\n:class: dropdown\n\n`
  to_insert += `${FENCE3}{literalinclude} ${filename}\n${FENCE3}\n\n${FENCE4}\n`
  const new_source = `${begin}${to_insert}${end}`
  model.sharedModel.setSource(new_source)
}
### To-dos

- switch data retrieval functions to parallel execution
- add local storage of data, so that retrieval functions stream to a file as
  opposed to loading everything into memory. for json data it is reasonable
  (and fast) to use json.dumps

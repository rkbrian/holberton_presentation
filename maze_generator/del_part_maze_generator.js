
  
  getKeyLocation() {

    let fromEntrance = this.initArray();
    let fromExit = this.initArray();

    this.totalSteps = -1;

    for(let j = 1; j < this.cols-1; j++) {
      if(this.maze[this.rows-1][j].includes("entrance")) {
        this.countSteps(fromEntrance, this.rows-1, j, 0, "exit");
      }
      if(this.maze[0][j].includes("exit")) {
        this.countSteps(fromExit, 0, j, 0, "entrance");
      }
    }

    let fc = -1, fr = -1;

    this.maze.forEach((row, r) => {
      row.forEach((cell, c) => {
        if(typeof fromEntrance[r][c] == "undefined") {
          return;
        }
        let stepCount = fromEntrance[r][c] + fromExit[r][c];
        if(stepCount > this.totalSteps) {
          fr = r;
          fc = c;
          this.totalSteps = stepCount;
        }
      });
    });

    return [fr, fc];
  }
  
  placeKey() {

    let fr, fc;
    [fr, fc] = this.getKeyLocation();

    this.maze[fr][fc] = ["key"];

  }

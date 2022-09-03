import React from "react";

const Project = ({ id, projectname, budgetalloted, budgetspent }) => {
  return (
    <div className="card">
      <h1 className="title">{projectname}</h1>

      <div className="right-top">
        <input type="range" className="slider" min="0" max={budgetalloted} value={budgetspent}></input>
        <h3 className="fundStatus">{budgetspent} / {budgetalloted}</h3>
      </div>

    </div>
  );
};

export default Project;

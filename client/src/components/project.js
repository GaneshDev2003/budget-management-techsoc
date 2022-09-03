import React from "react";

const Project = ({ id, projectname, budgetalloted, budgetspent }) => {
  return (
    <div className="card">
      <h1 className="title">{projectname}</h1>
      <h3 className="alloted"> {budgetalloted} </h3>
      <h3 className="used"> {budgetspent}</h3>
    </div>
  );
};

export default Project;

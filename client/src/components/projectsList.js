import React from "react";
import Project from "./project";

const ProjectList = ({ projects }) => {
  const projectArray = projects.map((user, i) => {
    return (
      <Project
        key={i}
        id={projects[i].id}
        projectname={projects[i].projectname}
        budgetalloted={projects[i].budgetalloted}
        budgetspent={projects[i].budgetspent}
      />
    );
  });
  return <div>{projectArray}</div>;
};

export default ProjectList;

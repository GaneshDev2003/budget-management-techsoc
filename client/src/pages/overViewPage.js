import React, { Component } from "react";
import ProjectList from "../components/projectsList";
import projects from "../components/projects_db";

class OverViewPage extends Component {
  constructor() {
    super();
    this.state = {
      projects: [],
      searchField: "",
    };
  }

  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((users) => this.setState({ projects: users }));
  }

  render() {
    return (
      <div className="tc">
        <h1 className="f1">Projects</h1>
        <ProjectList projects={projects} />;
      </div>
    );
  }
}

export default OverViewPage;

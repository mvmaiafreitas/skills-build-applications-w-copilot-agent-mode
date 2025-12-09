import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched Workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Workouts</h2>
        <table className="table table-striped table-bordered">
          <thead className="table-primary">
            <tr>
              <th>Name</th>
              <th>Type</th>
              <th>Duration</th>
              <th>Intensity</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={workout.id || idx}>
                <td>{workout.name || JSON.stringify(workout)}</td>
                <td>{workout.type}</td>
                <td>{workout.duration}</td>
                <td>{workout.intensity}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="btn btn-warning">Add Workout</button>
      </div>
    </div>
  );
};

export default Workouts;

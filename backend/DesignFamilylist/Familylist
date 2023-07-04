import React from 'react';

const familyMembers = [
  { id: 1, name: 'John Doe', age: 35, relationship: 'Father' },
  { id: 2, name: 'Jane Doe', age: 32, relationship: 'Mother' },
  { id: 3, name: 'Jack Doe', age: 10, relationship: 'Son' },
  { id: 4, name: 'Jill Doe', age: 8, relationship: 'Daughter' }
];

const FamilyMembersList = () => {
  return (
    <div>
      <h1>Family Members List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Relationship</th>
          </tr>
        </thead>
        <tbody>
          {familyMembers.map(member => (
            <tr key={member.id}>
              <td>{member.id}</td>
              <td>{member.name}</td>
              <td>{member.age}</td>
              <td>{member.relationship}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FamilyMembersList;


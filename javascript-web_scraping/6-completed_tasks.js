#!/usr/bin/node
// computes number of tasks computed by each user_id
// website given as {argument 1]}

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const allJobs = (JSON.parse(body));
  // console.log(allJobs)
  const userObj = {};
  for (const task in allJobs) {
    // console.log(allJobs[task])
    if (allJobs[task].completed === true) {
      const userId = allJobs[task].userId;
      const hasKey = userId in userObj;
      if (hasKey) {
        userObj[userId] += 1;
      } else {
        userObj[userId] = 1;
      }
    }
  }
  console.log(userObj);
});

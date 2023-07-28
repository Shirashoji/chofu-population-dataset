const year = 2021;
const fs = require("fs");

const data = JSON.parse(fs.readFileSync(`./data/${year}.json`, "utf8"));

function convert(input) {
  let output = [];
  for (let i = 0; i < input.length; i++) {
    const populationData = input[i];
    const sum = populationData.data
      .map((e) => [e.male, e.female])
      .flat()
      .reduce((sum, element) => sum + element, 0);

    output.push({
      town: populationData.town,
      data: [
        ...populationData.data.map(({ ageGroup, male, female }) => ({
          ageGroup,
          male: male / sum,
          female: female / sum,
        })),
      ],
    });
  }
  return output;
}

const convertData = JSON.stringify(convert(data));
fs.writeFileSync(`./normalized/${year}.json`, convertData);

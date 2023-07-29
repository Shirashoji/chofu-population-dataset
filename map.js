const year = process.argv[2];
const fs = require("fs");

const data = JSON.parse(fs.readFileSync(`./normalized/${year}.json`, "utf8"));

function convert(input) {
  let output = [];
  const chofu = input.filter((e) => e.town === "市内全域")[0];
  const populationData = input.filter((e) => e.town !== "市内全域");

  const ageGroups = [
    "0-4",
    "5-9",
    "10-14",
    "15-19",
    "20-24",
    "25-29",
    "30-34",
    "35-39",
    "40-44",
    "45-49",
    "50-54",
    "55-59",
    "60-64",
    "65-69",
    "70-74",
    "75-79",
    "80-84",
    "85-89",
    "90-94",
    "95-99",
    "100+",
  ];

  for (let i = 0; i < populationData.length; i++) {
    const town = populationData[i];
    if (town.town === "市内全域") continue;
    if (Math.max(...town.data.map((e) => [e.male, e.female]).flat()) === 0)
      continue;
    const sumofFeat = ageGroups
      .map((e) => {
        // console.log(e);
        // // console.log(town.data.filter((item) => item.ageGroup === e));
        // console.log(chofu.data.filter((item) => item.ageGroup === e));
        return (
          Math.pow(
            town.data.filter((item) => item.ageGroup === e)[0].male -
              chofu.data.filter((item) => item.ageGroup === e)[0].male,
            2
          ) +
          Math.pow(
            town.data.filter((item) => item.ageGroup !== e)[0].female -
              chofu.data.filter((item) => item.ageGroup === e)[0].female,
            2
          )
        );
      })
      .reduce((sum, element) => sum + element, 0);

    output.push({ town: town.town, value: sumofFeat });
  }
  return output;
}

const convertData = JSON.stringify(convert(data));
// console.log(convertData);
fs.writeFileSync(`./mapFeature/${year}.json`, convertData);

const year = 2021;

const fs = require("fs");

const data = JSON.parse(fs.readFileSync(`./rawJSON/${year}.json`, "utf8"));
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

function convert(input) {
  let arr = [];
  for (let i = 0; i < input.length; i++) {
    const keys = Object.keys(input[i]);
    const rawData = Object.fromEntries(
      keys
        .filter((key) => key !== "町丁")
        .map((key) => {
          return [key, input[i][key]];
        })
    );
    arr.push({
      town: input[i]["町丁"],
      data: ageGroups.map((age) => {
        const reAge = age
          .replace(/(\d*)-(\d*)/g, "$1～$2歳")
          .replace(/(\d*)\+/g, "$1歳以上");
        return {
          ageGroup: age,
          male: Number(rawData[`${reAge}（男）`]),
          female: Number(rawData[`${reAge}（女）`]),
        };
      }),
    });
  }
  return arr;
}

// console.log(convert(data));
const convertData = JSON.stringify(convert(data));
fs.writeFileSync(`./data/${year}.json`, convertData);

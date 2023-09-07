function convert(input) {
    let output = [];
    for (let i = 0; i < input.length; i++) {
        // const populationData = input[i];
        // // const sum = populationData.data
        // //     .map((e) => [e.male, e.female])
        // //     .flat()
        // //     .reduce((sum, element) => sum + element, 0);

        // output.push({
        //     town: populationData.town,
        //     data: [
        //         ...populationData.data.map(({ ageGroup, male, female }) => ({
        //             ageGroup,
        //             male: Math.atan(male / 2),
        //             female: Math.atan(female / 2),
        //         })),
        //     ],
        // });
        output.push({
            town: input[i].town,
            value: input[i].value,
        });
    }
    return output;
}

const fs = require("fs");

for (let year = 2017; year <= 2021; year++) {
    const data = JSON.parse(
        fs.readFileSync(`./mapFeature/${year}.json`, "utf8")
    );
    const convertData = JSON.stringify(convert(data));
    fs.writeFileSync(`./test/${year}.json`, convertData);
}

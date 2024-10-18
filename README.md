# Homework 1 - Data Engineering Course

This repository contains the source code for the first homework assignment of the Data Engineering course. The project was carried out by **Alessio Marinucci** and **Riccardo Felici**.

## Project Objective

The objective of this project is to extract specific data from HTML web pages using **XPath expressions**. The topic is related to **Computer Science**, and the data is extracted from research papers available on the website [arXiv.org](https://arxiv.org/).

## Topic Selection

We have chosen the topic of **Machine Translation (MT)** for this project and a total of 323 HTML files have been downloaded from arXiv.

## Data to be Extracted

For each research paper, the following elements are extracted using **XPath**:

- **Tables**: All the tables present in the paper.
- **Captions**: The captions associated with each table.
- **Footnotes**: Any footnotes present for the tables (if available).
- **Referenced Paragraphs**: Paragraphs that reference the specific table.

### Output Format

The extracted data is stored in a **JSON** file, ensuring that all relevant information for each paper is neatly organized and easily accessible.

---

## Example of JSON Structure

```json
{
    "1": {
        "table": "<table> ... </table>"
        "caption": "Table 1: Sample Data",
        "footnotes": "Footnote explaining the table",
        "referenced_paragraphs": [
          "This table highlights the key metrics used in AI research..."
          ]
      },
      "2": {
        "table": "<table> ... </table>"
        "caption": "Table 2: Model Performance",
        "footnotes": null,
        "referenced_paragraphs": [
          "In Table 2, we compare the performance of various models..."
        ]
      }
}
```

## Code Overview

This project involves the following steps:

1. **Scraping HTML Files**:
   The script downloads most relevant research papers in HTML format from [arXiv](https://arxiv.org/). The files are stored in a folder called `sources` for further analysis. The scraping process uses **BeautifulSoup** to parse the page and filter the links to the desired HTML files based on specific criteria.

2. **XPath Extraction**:
   Once the HTML files are downloaded, the next phase involves extracting specific data using **XPath** expressions. The goal is to extract:
   - **Tables**
   - **Captions** associated with the tables
   - **Footnotes** (if any)
   - **Referenced paragraphs** that mention the tables.

3. **Saving Data**:
   The extracted information is saved in a structured **JSON** file, ensuring easy access and further processing of the data.

5. **Automation**:
   The code is designed to automate the entire workflow, from downloading HTML files to extracting and storing relevant data. The script can handle multiple HTML files and be customized to adjust the number of files or different extraction needs.

## URL List

<details>
  <summary>Click me to expand URL list</summary>
https://arxiv.org/html/2405.09223.html
https://arxiv.org/html/2311.14465.html
https://arxiv.org/html/2402.18428.html
https://arxiv.org/html/2207.04900.html
https://arxiv.org/html/2311.08380.html
https://arxiv.org/html/2408.13831.html
https://arxiv.org/html/2402.13036.html
https://arxiv.org/html/2408.04216.html
https://arxiv.org/html/2310.14050.html
https://arxiv.org/html/2407.13469.html
https://arxiv.org/html/2208.05909.html
https://arxiv.org/html/2409.19523.html
https://arxiv.org/html/2310.13031.html
https://arxiv.org/html/2402.01416.html
https://arxiv.org/html/2311.16865.html
https://arxiv.org/html/2401.12873.html
https://arxiv.org/html/2408.11926.html
https://arxiv.org/html/2410.03278.html
https://arxiv.org/html/2410.07779.html
https://arxiv.org/html/2310.05025.html
https://arxiv.org/html/2305.11550.html
https://arxiv.org/html/2207.05851.html
https://arxiv.org/html/2310.14451.html
https://arxiv.org/html/2311.11601.html
https://arxiv.org/html/2406.18528.html
https://arxiv.org/html/2406.19478.html
https://arxiv.org/html/2311.07941.html
https://arxiv.org/html/2311.00998.html
https://arxiv.org/html/2401.05811.html
https://arxiv.org/html/2404.06107.html
https://arxiv.org/html/2406.07440.html
https://arxiv.org/html/2403.05257.html
https://arxiv.org/html/2404.04279.html
https://arxiv.org/html/2310.16417.html
https://arxiv.org/html/2404.14680.html
https://arxiv.org/html/2402.02633.html
https://arxiv.org/html/2310.07081.html
https://arxiv.org/html/2403.12666.html
https://arxiv.org/html/2401.06568.html
https://arxiv.org/html/2406.12419.html
https://arxiv.org/html/2209.03316.html
https://arxiv.org/html/2310.12127.html
https://arxiv.org/html/2409.02712.html
https://arxiv.org/html/2310.10385.html
https://arxiv.org/html/2405.11668.html
https://arxiv.org/html/2407.06230.html
https://arxiv.org/html/2403.01196.html
https://arxiv.org/html/2410.00545.html
https://arxiv.org/html/2408.11382.html
https://arxiv.org/html/2311.08306.html
https://arxiv.org/html/2406.01441.html
https://arxiv.org/html/2406.00787.html
https://arxiv.org/html/2402.10699.html
https://arxiv.org/html/2401.05176.html
https://arxiv.org/html/2311.10765.html
https://arxiv.org/html/2311.07066.html
https://arxiv.org/html/2310.14644.html
https://arxiv.org/html/2405.11942.html
https://arxiv.org/html/2310.05294.html
https://arxiv.org/html/2402.07681.html
https://arxiv.org/html/2409.13523.html
https://arxiv.org/html/2408.11457.html
https://arxiv.org/html/2401.16086.html
https://arxiv.org/html/2309.12491.html
https://arxiv.org/html/2409.15879.html
https://arxiv.org/html/2404.07851.html
https://arxiv.org/html/2410.05183.html
https://arxiv.org/html/2407.05319.html
https://arxiv.org/html/2407.05154.html
https://arxiv.org/html/2311.15507.html
https://arxiv.org/html/2407.02208.html
https://arxiv.org/html/2406.12364.html
https://arxiv.org/html/2407.03277.html
https://arxiv.org/html/2312.04807.html
https://arxiv.org/html/2408.17308.html
https://arxiv.org/html/2410.03277.html
https://arxiv.org/html/2407.02894.html
https://arxiv.org/html/2403.09832.html
https://arxiv.org/html/2310.17133.html
https://arxiv.org/html/2401.05861.html
https://arxiv.org/html/2404.02393.html
https://arxiv.org/html/2312.12740.html
https://arxiv.org/html/2312.07250.html
https://arxiv.org/html/2408.04872.html
https://arxiv.org/html/2409.05224.html
https://arxiv.org/html/2406.14267.html
https://arxiv.org/html/2402.02084.html
https://arxiv.org/html/2408.05738.html
https://arxiv.org/html/2310.20201.html
https://arxiv.org/html/2311.02310.html
https://arxiv.org/html/2310.14262.html
https://arxiv.org/html/2209.07351.html
https://arxiv.org/html/2405.13984.html
https://arxiv.org/html/2401.00751.html
https://arxiv.org/html/2403.00144.html
https://arxiv.org/html/2409.17673.html
https://arxiv.org/html/2403.03521.html
https://arxiv.org/html/2410.05047.html
https://arxiv.org/html/2311.03767.html
https://arxiv.org/html/2209.08827.html
https://arxiv.org/html/2410.07830.html
https://arxiv.org/html/2406.07970.html
https://arxiv.org/html/2209.09368.html
https://arxiv.org/html/2312.03710.html
https://arxiv.org/html/2401.07696.html
https://arxiv.org/html/2401.06468.html
https://arxiv.org/html/2401.05596.html
https://arxiv.org/html/2403.09259.html
https://arxiv.org/html/2401.13165.html
https://arxiv.org/html/2403.19142.html
https://arxiv.org/html/2312.07419.html
https://arxiv.org/html/2402.19267.html
https://arxiv.org/html/2405.15070.html
https://arxiv.org/html/2310.11360.html
https://arxiv.org/html/2401.17099.html
https://arxiv.org/html/2408.01394.html
https://arxiv.org/html/2405.08477.html
https://arxiv.org/html/2312.12056.html
https://arxiv.org/html/2207.04206.html
https://arxiv.org/html/2404.00397.html
https://arxiv.org/html/2310.13448.html
https://arxiv.org/html/2310.15612.html
https://arxiv.org/html/2408.16440.html
https://arxiv.org/html/2407.20438.html
https://arxiv.org/html/2404.02835.html
https://arxiv.org/html/2305.13504.html
https://arxiv.org/html/2310.12303.html
https://arxiv.org/html/2408.03150.html
https://arxiv.org/html/2406.08255.html
https://arxiv.org/html/2311.00508.html
https://arxiv.org/html/2405.12915.html
https://arxiv.org/html/2404.11201.html
https://arxiv.org/html/2405.11819.html
https://arxiv.org/html/2405.08172.html
https://arxiv.org/html/2309.07615.html
https://arxiv.org/html/2404.18413.html
https://arxiv.org/html/2407.18789.html
https://arxiv.org/html/2401.10016.html
https://arxiv.org/html/2401.16313.html
https://arxiv.org/html/2410.04075.html
https://arxiv.org/html/2401.04972.html
https://arxiv.org/html/2405.11937.html
https://arxiv.org/html/2401.05749.html
https://arxiv.org/html/2311.05379.html
https://arxiv.org/html/2406.02237.html
https://arxiv.org/html/2407.05489.html
https://arxiv.org/html/2312.04764.html
https://arxiv.org/html/2406.13698.html
https://arxiv.org/html/2209.14073.html
https://arxiv.org/html/2311.03696.html
https://arxiv.org/html/2405.19701.html
https://arxiv.org/html/2402.13331.html
https://arxiv.org/html/2404.05943.html
https://arxiv.org/html/2409.15051.html
https://arxiv.org/html/2311.02355.html
https://arxiv.org/html/2405.02887.html
https://arxiv.org/html/2406.07081.html
https://arxiv.org/html/2311.08538.html
https://arxiv.org/html/2403.19399.html
https://arxiv.org/html/2403.03075.html
https://arxiv.org/html/2410.07054.html
https://arxiv.org/html/2406.02267.html
https://arxiv.org/html/2404.14443.html
https://arxiv.org/html/2406.00049.html
https://arxiv.org/html/2406.11580.html
https://arxiv.org/html/2305.13204.html
https://arxiv.org/html/2208.06874.html
https://arxiv.org/html/2401.14559.html
https://arxiv.org/html/2310.19680.html
https://arxiv.org/html/2312.13179.html
https://arxiv.org/html/2404.01070.html
https://arxiv.org/html/2311.02765.html
https://arxiv.org/html/2409.13747.html
https://arxiv.org/html/2402.01772.html
https://arxiv.org/html/2404.15196.html
https://arxiv.org/html/2310.11163.html
https://arxiv.org/html/2405.02933.html
https://arxiv.org/html/2402.06894.html
https://arxiv.org/html/2403.09522.html
https://arxiv.org/html/2312.11852.html
https://arxiv.org/html/2402.01939.html
https://arxiv.org/html/2310.01188.html
https://arxiv.org/html/2312.00912.html
https://arxiv.org/html/2409.00071.html
https://arxiv.org/html/2311.07439.html
https://arxiv.org/html/2403.19285.html
https://arxiv.org/html/2407.06990.html
https://arxiv.org/html/2404.07673.html
https://arxiv.org/html/2312.14488.html
https://arxiv.org/html/2406.06073.html
https://arxiv.org/html/2404.13813.html
https://arxiv.org/html/2407.01126.html
https://arxiv.org/html/2410.03381.html
https://arxiv.org/html/2312.00214.html
https://arxiv.org/html/2310.08908.html
https://arxiv.org/html/2407.13579.html
https://arxiv.org/html/2409.14842.html
https://arxiv.org/html/2404.04846.html
https://arxiv.org/html/2408.11853.html
https://arxiv.org/html/2407.03076.html
https://arxiv.org/html/2209.03929.html
https://arxiv.org/html/2310.16924.html
https://arxiv.org/html/2403.06745.html
https://arxiv.org/html/2403.14118.html
https://arxiv.org/html/2405.07673.html
https://arxiv.org/html/2403.15469.html
https://arxiv.org/html/2309.11674.html
https://arxiv.org/html/2410.05472.html
https://arxiv.org/html/2311.18711.html
https://arxiv.org/html/2311.17492.html
https://arxiv.org/html/2402.16379.html
https://arxiv.org/html/2401.01283.html
https://arxiv.org/html/2401.05145.html
https://arxiv.org/html/2407.16266.html
https://arxiv.org/html/2401.17827.html
https://arxiv.org/html/2407.15154.html
https://arxiv.org/html/2207.11161.html
https://arxiv.org/html/2311.11976.html
https://arxiv.org/html/2209.08738.html
https://arxiv.org/html/2408.11512.html
https://arxiv.org/html/2402.14179.html
https://arxiv.org/html/2406.11632.html
https://arxiv.org/html/2409.02667.html
https://arxiv.org/html/2311.13475.html
https://arxiv.org/html/2310.05688.html
https://arxiv.org/html/2209.02906.html
https://arxiv.org/html/2311.03672.html
https://arxiv.org/html/2311.16362.html
https://arxiv.org/html/2409.05021.html
https://arxiv.org/html/2309.12863.html
https://arxiv.org/html/2310.20162.html
https://arxiv.org/html/2401.08350.html
https://arxiv.org/html/2404.04809.html
https://arxiv.org/html/2401.01419.html
https://arxiv.org/html/2406.10091.html
https://arxiv.org/html/2403.01580.html
https://arxiv.org/html/2401.06769.html
https://arxiv.org/html/2311.09389.html
https://arxiv.org/html/2406.06910.html
https://arxiv.org/html/2404.15332.html
https://arxiv.org/html/2404.08661.html
https://arxiv.org/html/2403.09740.html
https://arxiv.org/html/2409.04269.html
https://arxiv.org/html/2403.19161.html
https://arxiv.org/html/2406.06131.html
https://arxiv.org/html/2312.00536.html
https://arxiv.org/html/2311.14530.html
https://arxiv.org/html/2312.12588.html
https://arxiv.org/html/2410.06338.html
https://arxiv.org/html/2401.15360.html
https://arxiv.org/html/2311.08249.html
https://arxiv.org/html/2401.08417.html
https://arxiv.org/html/2401.12097.html
https://arxiv.org/html/2406.02876.html
https://arxiv.org/html/2406.07239.html
https://arxiv.org/html/2402.06342.html
https://arxiv.org/html/2310.20620.html
https://arxiv.org/html/2407.00108.html
https://arxiv.org/html/2311.08324.html
https://arxiv.org/html/2311.09132.html
https://arxiv.org/html/2401.16078.html
https://arxiv.org/html/2404.19505.html
https://arxiv.org/html/2402.12730.html
https://arxiv.org/html/2312.15872.html
https://arxiv.org/html/2402.18747.html
https://arxiv.org/html/2406.12564.html
https://arxiv.org/html/2405.19290.html
https://arxiv.org/html/2407.16470.html
https://arxiv.org/html/2401.06688.html
https://arxiv.org/html/2209.13940.html
https://arxiv.org/html/2309.12998.html
https://arxiv.org/html/2401.16055.html
https://arxiv.org/html/2407.14295.html
https://arxiv.org/html/2402.15061.html
https://arxiv.org/html/2409.17943.html
https://arxiv.org/html/2401.08429.html
https://arxiv.org/html/2409.19877.html
https://arxiv.org/html/2209.02145.html
https://arxiv.org/html/2403.11896.html
https://arxiv.org/html/2310.15262.html
https://arxiv.org/html/2310.14921.html
https://arxiv.org/html/2409.10989.html
https://arxiv.org/html/2408.00397.html
https://arxiv.org/html/2404.08259.html
https://arxiv.org/html/2405.12669.html
https://arxiv.org/html/2405.08997.html
https://arxiv.org/html/2403.10963.html
https://arxiv.org/html/2305.14189.html
https://arxiv.org/html/2403.03582.html
https://arxiv.org/html/2406.02517.html
https://arxiv.org/html/2209.15236.html
https://arxiv.org/html/2407.19965.html
https://arxiv.org/html/2404.02392.html
https://arxiv.org/html/2402.10940.html
https://arxiv.org/html/2311.14838.html
https://arxiv.org/html/2312.06926.html
https://arxiv.org/html/2310.10482.html
https://arxiv.org/html/2405.05478.html
https://arxiv.org/html/2406.15741.html
https://arxiv.org/html/2410.05553.html
https://arxiv.org/html/2310.13362.html
https://arxiv.org/html/2409.17939.html
https://arxiv.org/html/2403.16777.html
https://arxiv.org/html/2402.09725.html
https://arxiv.org/html/2209.02962.html
https://arxiv.org/html/2403.13130.html
https://arxiv.org/html/2403.02367.html
https://arxiv.org/html/2310.13361.html
https://arxiv.org/html/2405.01280.html
https://arxiv.org/html/2309.10526.html
https://arxiv.org/html/2310.13588.html
https://arxiv.org/html/2403.04178.html
https://arxiv.org/html/2406.13363.html
https://arxiv.org/html/2404.16257.html
https://arxiv.org/html/2311.02851.html
https://arxiv.org/html/2404.06964.html
https://arxiv.org/html/2401.07456.html
https://arxiv.org/html/2312.03753.html
https://arxiv.org/html/2403.01479.html
https://arxiv.org/html/2310.12236.html
https://arxiv.org/html/2404.17968.html
https://arxiv.org/html/2403.18031.html
https://arxiv.org/html/2309.07098.html
</details>

## Stats
- Total number of HTML files: 323
- Average tables per file: ~11.17
- Tables without a body: ~25.10%
- Tables without paragraphs: ~42.05%
- Tables without footnotes: ~87.64%
- Average references per table: ~1.03

const { Builder, By } = require('selenium-webdriver');

async function findKeyword(driver, keyword) {
  const pageSource = await driver.getPageSource();
  return pageSource.includes(keyword);
}

async function countElem(driver, tagName) {
  const elements = await driver.findElements(By.tagName(tagName));
  return elements.length;
}

async function main() {
  // initialize browser
  const driver = await new Builder().forBrowser('chrome').build();

  // navigate to your website
  await driver.get('http://localhost:3000/');
  const rewardTime = 10;
  let totalRewardTime = 0;
  const keyword = 'robinhood';
  if (await findKeyword(driver, keyword)) {
    totalRewardTime += rewardTime;
    await driver.sleep(rewardTime * 1000);
  }

  const tags = ['img'];
  for (const tag of tags) {
    const numElements = await countElem(driver, tag);
    totalRewardTime += rewardTime * numElements;
  }

  await driver.quit();
  console.log('Presence Time:', totalRewardTime, 'seconds');
}

if (require.main === module) {
  main();
}


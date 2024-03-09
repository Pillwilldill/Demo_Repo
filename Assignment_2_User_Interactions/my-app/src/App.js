import logo from './logo.svg';
import './App.css';
import GOW from './images/GodOfWar.png'

function App() {
  return (
    <div className="App">
      <header className="App-header">
<div>
  {/*Title with three paragraphs underneath*/}
  <h1>About Me: Christopher Cao</h1>
  <p>Hello everyone, my name is Christopher Cao and I am in my 4th year at CSUSB. 
    I am a computer engineering major hoping to build a career
    from what I have learned from all my CSE courses. Depending on the job market's performance
    in the future, I may or may not be hired at a tech company for a tech related job such as a 
    data analyst. Even if I do not get hired by a tech company, I plan to use all the skills and 
    knowledge from my CSE courses to be able to work tech related jobs at companies that are not 
    neccessarily tech companies.</p>
  <p>In my free time, I enjoy playing video games and reading manga and webtoons. I enjoy genres such
    as action adventure and platforming although I am open to other genres. Recently I have been hooked
    onto cinematic adventure games such as God of War (2018) for their story telling and pushing the boundary 
    for what is possible in a video game. When it comes to manga and webtoons, I am biased toward romance
    as I enjoy watching the lead characters in comedic scenarios and how they overcome a variety of obstacles 
    to be able to remain as a couple.</p>
  <p>Along with playing video games and reading, I have been learning about long term financial stability
    on the side and have even begun investing in low cost index ETFs through the brokerage Robinhood. 
    While I am not double majoring in financial concentration, I believe I have adequate knowledge on topics 
    such as high yield savings accounts, certificates of deposits (CDS), high historical returns, and more. The 
    only difficult part so far is learning how to optimally budget between how much I can invest and 
    how mach I can immediately spend. </p>
  {/*Use of div to hold misc information about me*/}
  <h2>Extras:</h2>
  <div className="section">
    Fun Fact: I have over 15,000 songs held in one playlist.
  </div>
  <div className="section">
    Closing: I hope to meet the class' expectation of me and 
    to hopefully use what I learned in CSE 4500 in my
    future endeavors.
  </div>
  {/*Use of div to show image*/}
  <div>
    <img src={GOW} alt="GodOfWar" />
  </div>
  {/*Use of div to show github link*/}
  <div className="section">
    Github Link:
    <a href="https://github.com/Pillwilldill/Demo_Repo">GitHub Link</a>
  </div>
</div>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

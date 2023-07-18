
import Welcome from "./pages/welcome/Welcome";
import Home from "./pages/home/Home";



const isLogged = true;

function App() {
  return (
    <div className="App">
      {isLogged ? <Home /> : <Welcome />}
    </div>
  );
}

export default App;

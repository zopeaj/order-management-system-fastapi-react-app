import { Route, Routes, BrowserRouter} from "react-router-dom"
import { FixedPosition, ScrolledAppBar } from "../src/components/app_bar_comp";
import { screen, MyToolbar } from "../src/components/app_bar_navigation";
import { HomePage } from "../src/components/HomePage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="fixedPosition" element={<FixedPosition/>} />
        <Route path="scrolledappbar" element={<ScrolledAppBar/>} />
        <Route path="navigationapp" element={<MyToolbar/>} />
        <Route exact path="home" render={screen('Home', 'Home')} />
        <Route exact path="/page2" render={screen('Page 2', 'Page 2')} />
        <Route exact path="/page3" render={screen('Page 3', 'Page 3')} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

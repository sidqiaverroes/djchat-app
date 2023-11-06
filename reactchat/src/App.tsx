import { createBrowserRouter, Route, RouterProvider, createRoutesFromElements } from "react-router-dom"
import Home from "./pages/Home"
import Server from "./pages/Server"
import Explore from "./pages/Explore"
import ToggleColorMode from "./components/ToggleColorMode"

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<Home />} />
      <Route path="/server" element={<Server />} />
      <Route path="/explore/:categoryName" element={<Explore />} />
    </Route>
  )
)

const App = () => {
  return (
    <ToggleColorMode>
      <RouterProvider router={router} />
    </ToggleColorMode>
  )
}

export default App



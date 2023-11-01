import { createBrowserRouter, Route, RouterProvider, createRoutesFromElements } from "react-router-dom"
import Home from "./pages/Home"

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<Home />} />
    </Route>
  )
)

const App = () => {
  return <RouterProvider router={router} />
}

export default App



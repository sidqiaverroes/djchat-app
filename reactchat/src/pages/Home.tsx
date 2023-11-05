import {Box, CssBaseline} from "@mui/material"
import PrimaryAppBar from "./template/PrimaryAppBar"
import PrimaryDraw from "./template/PrimaryDraw"
import SecondaryDraw from "./template/SecondaryDraw"
import Main from "./template/Main"
import PopularChannels from "../components/PrimaryDraw/PopularChannels"
import ExploreCategories from "../components/SecondaryDraw/ExploreCategories"

const Home = () => {
  return (
    <Box sx={{display: "flex"}}>
        <CssBaseline />
        <PrimaryAppBar />
        <PrimaryDraw>
          <PopularChannels />
        </PrimaryDraw>
        <SecondaryDraw>
          <ExploreCategories />
        </SecondaryDraw>
        <Main />
    </Box>
  )
}

export default Home

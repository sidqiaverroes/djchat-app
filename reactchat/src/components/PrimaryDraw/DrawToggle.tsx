import { ChevronLeft } from "@mui/icons-material"
import { Box, IconButton } from "@mui/material"

const DrawToggle = () => {
  return (
    <Box sx={{height: "50px", display: "flex", alignItems: "center", justifyContent: "center"}}>
        <IconButton>
            <ChevronLeft />
        </IconButton>
    </Box>
  )
}

export default DrawToggle
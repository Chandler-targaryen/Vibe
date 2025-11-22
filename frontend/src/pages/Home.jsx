import { Box, Typography } from "@mui/material";
import logo from "../assets/logo.png";

export default function Home() {
  return (
    <Box
      sx={{
        background: "#f5f2eb",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <img src={logo} style={{ width: 150, marginBottom: 20 }} />

      <Typography
        variant="h4"
        sx={{
          fontWeight: 700,
          color: "#000"
        }}
      >
        Coming Soon
      </Typography>
    </Box>
  );
}
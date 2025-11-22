import { Card, Box } from "@mui/material";

export default function AuthCard({ children }) {
  return (
    <Box 
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        background: "#f5f2eb",
      }}
    >
      <Card
        sx={{
          width: 420,
          padding: 4,
          borderRadius: 4,
          background: "#ffffff",
          boxShadow: "0 0 40px rgba(0,0,0,0.08)"
        }}
      >
        {children}
      </Card>
    </Box>
  );
}
import { Button, Typography } from "@mui/material";
import AuthCard from "../components/AuthCard";
import TextFieldStyled from "../components/TextFieldStyled";
import logo from "../assets/logo.png";

export default function ForgotPassword() {
  return (
    <AuthCard>
      <img src={logo} style={{ width: 120, marginBottom: 20 }} />

      <Typography variant="h5" sx={{ fontWeight: 700, mb: 2 }}>
        Reset Password
      </Typography>

      <TextFieldStyled label="Email Address" />

      <Button
        fullWidth
        variant="contained"
        sx={{ mt: 2, mb: 2, bgcolor: "#000000" }}
      >
        Send Reset Link
      </Button>

      <Typography variant="body2" sx={{ textAlign: "center" }}>
        <a href="/login" style={{ color: "#000" }}>Back to login</a>
      </Typography>
    </AuthCard>
  );
}
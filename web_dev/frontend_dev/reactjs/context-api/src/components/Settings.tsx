import { useTheme } from "../hooks/use-theme";

const Settings = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <section>
      <p>Current theme: {theme}</p>

      <button onClick={toggleTheme}>
        Switch to {theme === "light" ? "dark" : "light"} mode
      </button>
    </section>
  );
}

export default Settings

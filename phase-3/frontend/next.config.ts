import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    serverActions: {},
  },
  // Ensure proper asset prefix for Vercel
  assetPrefix: process.env.NODE_ENV === 'production' ? '' : undefined,
};

export default nextConfig;

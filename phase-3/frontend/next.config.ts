import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'standalone',
  experimental: {
    serverActions: {},
  },
  // Remove asset prefix to ensure assets are served correctly in Docker
  // assetPrefix: process.env.NODE_ENV === 'production' ? '' : undefined,
};

export default nextConfig;

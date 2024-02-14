import java.util.Comparator;

public class PointXComparator implements Comparator<Point> {
    @Override
    public int compare(Point firstPoint, Point secondPoint) {
        return Double.compare(firstPoint.x, secondPoint.x);
    }
}
